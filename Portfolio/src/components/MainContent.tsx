import "./MainContent.css";

const MainContent = () => {
  return (
    <>
      <div className="main-content">
        <div className="main-img">
          <img src="./pictures/Me.jpg" alt="Jacob Clostio" />
        </div>
        <div className="main-text shadow-lg p-3 mb-5 bg-aqua rounded">
          <h1>
            <b>Hi, my name is </b>
            <span>
              <b className="nameBackground">Jacob Clostio</b>
            </span>
          </h1>
          <p className="main-text-box">
          I graduated from Montana State University with a major in Computer Science and a minor in Mathematics.
          After college, I worked at a startup developing agency management systems for insurance companies.
          Currently, I am a full-stack developer, focusing on P&C Policy administration software.
          </p>
        </div>
      </div>
    </>
  );
};
export default MainContent;
