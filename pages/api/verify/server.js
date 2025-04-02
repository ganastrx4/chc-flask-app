require("dotenv").config();
const express = require("express");
const cors = require("cors");
const fetch = require("node-fetch");

const app = express();
app.use(express.json());
app.use(cors());

// Ruta de verificación de World ID
app.post("/api/verify", async (req, res) => {
    const { world_id, proof, action_id, signal } = req.body;

    // Verifica que todos los parámetros necesarios estén presentes
    if (!world_id || !proof || !action_id || !signal) {
        return res.status(400).json({ success: false, message: "Faltan parámetros necesarios (world_id, proof, action_id, signal)" });
    }

    try {
        // Llamada a la API de Worldcoin para verificar el World ID
        const response = await fetch("https://id.worldcoin.org/verify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ world_id, proof, action_id, signal }),
        });

        // Procesa la respuesta de la API de Worldcoin
        const data = await response.json();

        // Verifica si la respuesta indica que la verificación fue exitosa
        if (data.success) {
            return res.status(200).json({ success: true, message: "Verificación exitosa" });
        } else {
            return res.status(400).json({ success: false, message: "No se pudo verificar el World ID" });
        }
    } catch (error) {
        console.error("Error al verificar World ID:", error);
        return res.status(500).json({ success: false, message: "Error en el servidor" });
    }
});

// Configuración del puerto del servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor escuchando en el puerto ${PORT}`);
});

// pages/verify.js

"use client";
import { IDKitWidget, VerificationLevel } from '@worldcoin/idkit';

const VerifyPage = () => {
  const verifyProof = async (proof) => {
    try {
      // Enviar el proof al servidor para su verificación
      const response = await fetch('/verify-proof', {
        method: 'POST',
        body: JSON.stringify({ proof }),
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const result = await response.json();

      if (result.message === "Verificación exitosa") {
        console.log("Usuario verificado");
      } else {
        console.log("Proof no válido");
      }
    } catch (error) {
      console.error("Error al verificar:", error);
    }
  };

  const onSuccess = () => {
    console.log("Verificación exitosa!");
    // Aquí puedes agregar acciones que ocurran después de la verificación
  };

  return (
    <div>
      <h1>Verificación con Worldcoin</h1>
      <IDKitWidget
        app_id="app_7686f9027d3e3c0b53d987a3caf1e111"
        action="user_login"
        verification_level={VerificationLevel.Device}
        handleVerify={verifyProof}
        onSuccess={onSuccess}
      >
        {({ open }) => (
          <button onClick={open}>Verificar con World ID</button>
        )}
      </IDKitWidget>
    </div>
  );
};

export default VerifyPage;

