import "./Footer.css";
const Footer = () => {
  return (
    <>
      <hr className="footer-hr"></hr>
      <div className="contact-container">
        <div>jacobclostio@gmail.com</div>
        <div>
          <a href="https://www.linkedin.com/in/jacob-clostio-aa8064195/">
            LinkedIn
          </a>
        </div>
        <div>
          <a href="https://github.com/Jclostio/Projects">Github Projects</a>
        </div>
        <div>© 2023 Jacob Clostio using React</div>
      </div>
    </>
  );
};
export default Footer;
