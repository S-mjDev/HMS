import { Navbar as ReactstrapNavbar, NavbarBrand } from "reactstrap";

function Navbar({ onPageChange }) {
  return (
    <div>
      <nav className="navbar">
        <span><img src="./QPHN_LOGO.jpg" alt="QPHN Logo" className="logo" /> </span><NavbarBrand><h1>Quezon Provincial Hospital Network-Bonpen (Catanauan)</h1> </NavbarBrand>
          
      <ReactstrapNavbar>

      <ul className="nav-links">
        <li><button onClick={() => onPageChange('home')}>Home</button></li>
        <li><button onClick={() => onPageChange('search')}>Search</button></li>
        <li><button onClick={() => onPageChange('patient registration')}>Patient Registration</button></li>
        <li><button onClick={() => onPageChange('services')}>Services</button></li>
        <li><button onClick={() => onPageChange('contact')}>Contact</button></li>
      </ul>
      </ReactstrapNavbar>
      </nav>
    </div>
  );
}

export default Navbar;