const qrcode = require("qrcode-terminal");
// import qrcode from "qrcode-terminal"
// import {analzyer} from "./utils/analyzer.js";
const {  base64ToImage } = require("./utils/actions.js");
const { UrlLinks } = require("./utils/UrlLinks.js");
const { Client, MessageMedia, LocalAuth } = require("whatsapp-web.js");
// import { Client, MessageMedia, LocalAuth } from "whatsapp-web.js";
const client = new Client({ authStrategy: new LocalAuth() });
// const media = MessageMedia.fromFilePath("./image.png");
process.on('uncaughtException', function (err) {
  console.error(err);
  console.log("Node NOT Exiting...");
});

console.log("Starting script...");

client.on("qr", (qr) => {
  console.log("QR RECEIVED", qr);
  qrcode.generate(qr, { small: true });
});

client.on("ready", () => {
  console.log("Client is ready!");
});

// client.on("message", (message) => {
//   console.log(message);
// });

// client.on("message", (message) => {
//   if (message.body === "!ping") {
//     message.reply("pong");
//   }
// });

// client.on("message", (message) => {
//   if (message.body === "!image") {
//     client.sendMessage(message.from, media);
//   }
// });

client.on("message", async (message) => {
  if (UrlLinks.urlFromMsg(message.body) !== null) {

    //summary
    const msg = await UrlLinks.summary(UrlLinks.urlFromMsg(message.body));
    message.reply(`*Summarization of linked article*\n` + msg);
    // message.reply(analzyer(message.body));
    
  //twitter analysis
  const twitter = await UrlLinks.twitterAnalysis(UrlLinks.urlFromMsg(message.body));
  const twitterMsg = `*Twitter Analysis*
Total Tweets: ${twitter.count},
Total ReTweets: ${twitter.retweet},
Total Likes: ${twitter.likecount},
Hashtags: ${twitter.hashtags.join("  ")}
  `;
  client.sendMessage(message.from, twitterMsg);

  //twitter bot activity
  const botAcivity = await UrlLinks.botAcivity(UrlLinks.urlFromMsg(message.body));
  const botActivityMsg = `
  *Bot Activity Analysis*
  ${botAcivity.flag ? "Bot Activity Detected" : "No Bot Activity Detected"}
  ${
    botAcivity.flag ?
    "\n*Users displaying bot behaviour*:\n " + botAcivity.bots.join("  ") 
    : ""
  }
  `;
  client.sendMessage(message.from, botActivityMsg);
  
  // authenticity check
  const authenticity = await UrlLinks.authenticity(UrlLinks.urlFromMsg(message.body));
  const authenticityMsg = 
  `*Authenticity Check*
  ${authenticity.flag ? "Authentic Source of Information" : "Source of Information is blacklisted"}
  _based on google's list of blacklisted news sources_
  `
  
  // propaganda check
  // const propaganda = await UrlLinks.propogandaCheck(UrlLinks.urlFromMsg(message.body));
  // console.log(propaganda)
  // // const propogandaMedia = new MessageMedia("image/png", propaganda);
  // base64ToImage(propaganda, "./propaganda.png");
  // try {
    //   const media = MessageMedia.fromFilePath("./propaganda.png");
    //   client.sendMessage(message.from, propogandaMedia);
    // } catch {
      //   console.log("propoganda image failed")
      // }
      
      
      // twitter senitment image
      // const twitterSentiment = await UrlLinks.twitterSentiment(UrlLinks.urlFromMsg(message.body));
      // console.log(twitterSentiment)
      // const twitterImage = new MessageMedia("image/png", twitterSentiment);
      // base64ToImage(twitterSentiment, "./twitterSentiment.png");
      // const media = MessageMedia.fromFilePath("./twitterSentiment.png");
      // client.sendMessage(message.from, media);
      
      
    } else {
      
    }

});

// console.log(analzyer("hello world"))

client.initialize();

