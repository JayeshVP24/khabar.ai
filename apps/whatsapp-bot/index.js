const qrcode = require("qrcode-terminal");
// import qrcode from "qrcode-terminal"
// import {analzyer} from "./utils/analyzer.js";
const { isUrl } = require("./utils/actions.js");
const { Client, MessageMedia, LocalAuth } = require("whatsapp-web.js");
// import { Client, MessageMedia, LocalAuth } from "whatsapp-web.js";
const client = new Client({ authStrategy: new LocalAuth() });
const media = MessageMedia.fromFilePath("./image.png");

console.log("Starting script...")

client.on("qr", (qr) => {
  console.log("QR RECEIVED", qr);
  qrcode.generate(qr, { small: true });
});

client.on("ready", () => {
  console.log("Client is ready!");
});

client.on("message", (message) => {
  console.log(message);
});

client.on("message", (message) => {
  if (message.body === "!ping") {
    message.reply("pong");
  }
});

client.on("message", (message) => {
  if (message.body === "!image") {
    client.sendMessage(message.from, media);
  }
});

client.on("message", (message) => {
    message.reply(analzyer(message.body));
})

console.log(analzyer("hello world"))

// client.initialize();