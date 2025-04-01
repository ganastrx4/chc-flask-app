export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: "Método no permitido" });
    }

    const { proof } = req.body;

    try {
        const response = await fetch("https://developer.worldcoin.org/api/verify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ proof }),
        });

        const data = await response.json();
        if (data.success) {
            return res.status(200).json({ success: true });
        } else {
            return res.status(400).json({ success: false });
        }
    } catch (error) {
        console.error("Error verificando World ID:", error);
        return res.status(500).json({ error: "Error interno del servidor" });
    }
}
