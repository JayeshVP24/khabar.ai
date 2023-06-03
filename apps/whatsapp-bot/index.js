const qrcode = require("qrcode-terminal");

const { Client, MessageMedia, LocalAuth } = require("whatsapp-web.js");
const client = new Client({ authStrategy: new LocalAuth() });
const media = MessageMedia.fromFilePath("./image.png");

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

client.initialize();
