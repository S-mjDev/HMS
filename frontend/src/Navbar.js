function Navbar({ onPageChange }) {
  return (
    <nav className="navbar">
      <h2  className="logo"><span><img src="./QPHN_LOGO.jpg" alt="QPHN Logo" className="logo" /></span>QPHN-Bonpen (Catanauan)</h2>
      <ul className="nav-links">
        <li><button onClick={() => onPageChange('home')}>Home</button></li>
        <li><button onClick={() => onPageChange('search')}>Search</button></li>
        <li><button onClick={() => onPageChange('patient registration')}>Patient Registration</button></li>
        <li><button onClick={() => onPageChange('services')}>Services</button></li>
        <li><button onClick={() => onPageChange('contact')}>Contact</button></li>
      </ul>
    </nav>
  );
}

export default Navbar;