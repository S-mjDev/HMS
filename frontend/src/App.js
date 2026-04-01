import { useState } from 'react';
import Navbar from "./Navbar";
import PatientRegistration from "./components/PatientRegistration";
import SearchBar from './components/SearchBar';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query) => {
    if (!query.trim()) {
      setResults([]);
      return;
    }

    setLoading(true);

    try {
      const res = await fetch(`http://localhost:8000/patient/?search=${query}`);
      const data = await res.json();
      let resultsArray = [];
      if (Array.isArray(data)) {
        resultsArray = data;
      } else if (data && Array.isArray(data.results)) {
        resultsArray = data.results;
      } else if (data && typeof data === 'object') {
        resultsArray = [data];
      }
      setResults(resultsArray);
    } catch (err) {
      console.error(err);
      setResults([]);
    } finally {
      setLoading(false);
    }
  };


  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'search':
        return (
          <>
            <SearchBar onSearch={handleSearch} />
            {loading && <p>Loading...</p>}
            <SearchResults results={results} />
          </>
        );
      case 'patient registration':
        return <PatientRegistration />;
      case 'services':
        return <Services />;
      case 'contact':
        return <Contact />;
      default:
        return <Home />;
    }
  };

  return (
    <div>
      <Navbar onPageChange={setCurrentPage} />
      {renderPage()}
    </div>
  );
}

function Home() {
  return (
    <div>
      <h1> Welcome to the Home Page</h1>
      <p>This is the Hospital Management System.</p>
    </div>
  );
}




function Services() {
  return (
    <div>
      <h1>Services</h1>
      <p>Our hospital services.</p>
    </div>
  );
}

function Contact() {
  return (
    <div>
      <h1>Contact Us</h1>
      <p>Get in touch with us.</p>
    </div>
  );
}

function SearchResults({ results }) {
  if (!Array.isArray(results) || results.length === 0) {
    return null;
  }

  return (
    <div className="search-results">
      <h2>Search Results</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Address</th>
            <th>Birthday</th>
          </tr>
        </thead>
        <tbody>
          {results.map((item, index) => {
            const firstName = item.firstname || item.first_name || item.name || '';
            const midName = item.midname || item.middle_name || '';
            const lastName = item.lastname || item.last_name || '';
            const patientName = [firstName, midName, lastName].filter(Boolean).join(' ') || item.patient_name || item.name || 'Unknown';

            return (
              <tr key={item.id || index}>
                <td>{item.id || '—'}</td>
                <td>{patientName}</td>
                <td>{item.address || '—'}</td>
                <td>{item.birthday || '—'}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default App;

