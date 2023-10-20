import "bootstrap/dist/css/bootstrap.css";
import "./Navbar.css";
import { useEffect, useState } from "react";

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        setIsScrolled(true); // Set state to indicate that the user has scrolled
      } else {
        setIsScrolled(false); // Set state to indicate that the user is at the top
      }
    };

    window.addEventListener("scroll", handleScroll);

    // Cleanup the event listener when the component unmounts
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div>
      <nav className={`navbar ${isScrolled ? "scrolled" : ""}`}>
        <div className="container-fluid">
          <a className="navbar-brand" href="/">
            <img src="./pictures/logo.png" alt="Jacob Clostio" />
          </a>
          <ul className="nav justify-content-center">
            <li className="nav-item">
              <a className="nav-link" href="#/about">
                About
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#/projects">
                Projects
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="./Resume.pdf" target="_blank">
                Resume
              </a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
