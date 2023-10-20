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
            I'm a recent graduate from Montana State University, holding a
            Bachelor's degree in Computer Science and a minor in Mathematics.
            Currently, I am working at a startup software company focusing on
            developing agency management systems for insurance companies.
            However, I'm now in search of a fresh challenge where I can further
            my skills, contribute to a larger team, and be part of a broader
            mission. I'm enthusiastic about exploring new opportunities and
            would welcome the chance to connect.
          </p>
        </div>
      </div>
    </>
  );
};
export default MainContent;
