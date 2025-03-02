import React, { useState } from "react";
import axios from "axios";
import "./StockPredictor.css"; // Import CSS for dark theme

const StockPredictor = () => {
    const [date, setDate] = useState("");
    const [predictions, setPredictions] = useState([]);
    const [error, setError] = useState("");

    const handlePredict = async () => {
        if (!date) {
            setError("Please select a date.");
            return;
        }
        setError("");

        try {
            const response = await axios.post("http://localhost:5000/predict", { date });
            setPredictions(response.data);
        } catch (err) {
            setError("Failed to fetch predictions.");
            console.error(err);
        }
    };

    return (
        <div className="container">
            <h1>Stock Price Prediction</h1>

            <div className="input-container">
                <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    className="date-input"
                />
                <button onClick={handlePredict} className="submit-btn">
                    Submit
                </button>
            </div>

            {error && <p className="error">{error}</p>}

            {predictions.length > 0 && (
                <div className="result-container">
                    <h2>Predicted Prices</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Stock</th>
                                <th>Predicted Price</th>
                                <th>Accuracy</th>
                            </tr>
                        </thead>
                        <tbody>
                            {predictions.map((stock, index) => (
                                <tr key={index}>
                                    <td>{stock.stock}</td>
                                    <td>${stock.predicted_price}</td>
                                    <td>{(stock.accuracy * 100).toFixed(2)}%</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default StockPredictor;
