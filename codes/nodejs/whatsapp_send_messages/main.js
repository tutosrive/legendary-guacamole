import pkg from "whatsapp-web.js";
import qrcode from "qrcode-terminal"; // Para login con app whatsapp android
import fs from "node:fs";
import { executablePath } from "puppeteer";

const { Client, LocalAuth } = pkg;
let channel_id = "chat_id@newsletter";
let DATA = null;

// Solo es de el uso que dí, pued hacerse un socket en lugar de un archivo estático
fs.readFile("./data/messages.json", "utf8", (err, data) => {
  if (err) {
    console.error("Error al leer archivo:", err);
    process.exit(1);
  }
  try {
    DATA = JSON.parse(data);
    console.log("Cargados", DATA.length, "mensajes.");
  } catch (parseErr) {
    console.error("Error en JSON:", parseErr);
    process.exit(1);
  }
});

const client = new Client({
  puppeteer: {
    executablePath: executablePath(),
  },
  authStrategy: new LocalAuth(),
});

client.on("qr", (qr) => {
  qrcode.generate(qr, { small: true });
  console.log("Escanea este QR con WhatsApp.");
});

client.on("ready", async () => {
  console.log("Cliente listo! Enviando mensajes...");

  // ¡IMPORTANTE!

  // Este bloque de código comentado, es para obtener los ID de un chat especifico (en este caso un canal...)
  // Descomentar para ver... 


  // const chats = await client.getChannels();
  // chats.forEach((chat) => {
  //   if (chat.isChannel && chat.name === "OpenLab Tools") {
  //     console.log(`Canal: ${chat.name} - ID: ${chat.id._serialized}`);
  //   }
  // });

  // Envía automáticamente, se puede re-escribir la lógica
  sendMessages();
});

client.on("auth_failure", (msg) => {
  console.error("Fallo de auth:", msg);
  process.exit(1);
});

client.on("disconnected", (reason) => {
  console.log("Desconectado:", reason);
  process.exit(1);
});

client.initialize();

async function sendMessages() {
  if (!channel_id) {
    console.error("¡Configura channel_id primero!");
    process.exit(1);
  }
  if (!DATA || !Array.isArray(DATA)) {
    console.error("Mensajes no válidos del JSON.");
    process.exit(1);
  }

  const messages = DATA.map((item) => item.message);

  try {
    const chat = await client.getChatById(channel_id);
    if (!chat.isChannel) {
      throw new Error("No es un canal válido.");
    }

    for (const msg of messages) {
      await chat.sendMessage(msg);
      console.log(`Enviado: ${msg.substring(0, 50)}...`);
      // Se envía mensajes cada 3 segundos automáticamente
      await new Promise((resolve) => setTimeout(resolve, 3000)); // Delay anti-ban
    }
    console.log("¡Todos enviados!");
    process.exit(0);
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
}
