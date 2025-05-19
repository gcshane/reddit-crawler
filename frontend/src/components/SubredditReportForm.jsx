import React, { useState } from "react";
import axios from "axios";
import "./SubredditReportForm.css"; // <-- Import the CSS file

export default function SubredditReportForm() {
  const [username, setUsername] = useState("");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    try {
      const url = `/crawl/memes/20/day/${username}`;
      await axios.get(url);

      setMessage("✅ Report successfully sent via Telegram!");
    } catch (err) {
      console.error(err);
      setMessage("❌ Failed to send report. Check server/API.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>📈 What's trending on r/memes?</h2>
      <p>
        Make sure to /start the{" "}
        <a href="https://t.me/shanes_reddit_crawler_bot" target="_blank" rel="noopener noreferrer">
          bot
        </a>{" "}
        first!
      </p>
      <form onSubmit={handleSubmit}>
        <label>
          Telegram Username:
          <input
            className="full-width-input"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>

        <button className="full-width-input" type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Report"}
        </button>

        <p className="message">{message}</p>
      </form>
    </div>
  );
}