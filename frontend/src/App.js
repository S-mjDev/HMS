import { useState } from 'react';
import Navbar from "./Navbar";
import PatientRegistration from "./components/PatientRegistration";

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'search':
        return <Search />;
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

function Search() {
  
  return (
    <div>
      <h1>Search Page</h1>
      <p>Search for patients or doctors.</p>
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

export default App;

