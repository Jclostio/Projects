import Navbar from "./components/Navbar";
import MainContent from "./components/MainContent";
import Footer from "./components/Footer";
import Projects from "./components/Projects";
import About from "./components/About";

import { HashRouter as Router, Route, Routes } from "react-router-dom";
import FadeIn from "react-fade-in/lib/FadeIn";
import "./App.css";

function App() {
  return (
    <>
      <Router>
        <FadeIn>
          <Navbar />
          <Routes>
            <Route path="/" element={<MainContent />} />
            <Route path="/about" element={<About />} />
            <Route path="/projects" element={<Projects />} />
          </Routes>
          <Footer />
        </FadeIn>
      </Router>
    </>
  );
}

export default App;
