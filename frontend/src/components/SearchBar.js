import React, { useState } from "react";

function SearchBar({ onSearch = () => {} }) {
  const [input, setInput] = useState("");

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault(); // Prevents page reload
    const trimmed = input.trim();
    if (trimmed.length === 0) {
      return;
    }
    onSearch(trimmed);
  };

  return (
    <form className="search-container" onSubmit={handleSubmit}>
      <input
        id="search-input"
        type="text"
        placeholder="Search Patient Name..."
        value={input}
        onChange={handleChange}
      />
      <button className="search-button" type="submit">
        🔍
      </button>
    </form>
  );
}


export default SearchBar;