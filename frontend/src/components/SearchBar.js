import React, { useState } from "react";

function SearchBar({ onSearch = () => {} }) {
  const [input, setInput] = useState("");

  const handleChange = (e) => {
    const value = e.target.value;
    setInput(value);
    onSearch(value); // send data to parent
  };
  
  const handleSubmit = (event) => {
    event.preventDefault(); // Prevents page reload
    alert(`Searching for: ${input}`);
  };

  

  return (
    <form onSubmit={handleSubmit}>
    <div className="search-container">
    <input
      type="text"
      placeholder="Search..."
      value={input}
      onChange={handleChange}
    />
     <button className="search-button" type="submit">Submit</button>
    </div>
    </form>
  );
}


export default SearchBar;