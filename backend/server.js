const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();
const PORT = 5001;

// Middleware
app.use(cors());
app.use(express.json());

// POST endpoint to predict stock prices
app.post("/predict", (req, res) => {
    const { date } = req.body;

    if (!date) {
        return res.status(400).json({ error: "Date is required" });
    }

    // Run the Python script with the date as an argument
    const pythonProcess = spawn("python", ["model3.py", date]);

    let dataString = "";

    pythonProcess.stdout.on("data", (data) => {
        dataString += data.toString();
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on("close", (code) => {
        try {
            const predictions = JSON.parse(dataString);
            res.json(predictions);
        } catch (error) {
            res.status(500).json({ error: "Failed to process data" });
        }
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});


