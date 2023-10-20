import "./Projects.css";
import "./About.css";
import FadeIn from "react-fade-in/lib/FadeIn";

const Projects = () => {
  return (
    <>
      <FadeIn>
        <div className="project-header">
          <h1>
            <b>Projects</b>
          </h1>
          <h3>
            Source code can be found{" "}
            <a href="https://github.com/Jclostio/Projects" target="_blank">
              here
            </a>
          </h3>
        </div>
        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Neural Network Classification</b>
              </h2>
              <p>
                This project was a collaborative effort during my senior year
                machine learning course. Together with a peer, we designed and
                implemented a Neural Network from scratch, incorporating
                backpropagation with tunable parameters. Our primary objective
                was data classification, and we tested the network with both
                regression and classification datasets, continuously fine-tuning
                the parameters to achieve higher accuracy.
              </p>
              <p>
                The Neural Network's key tunable parameters included the number
                of hidden layers, the nodes per hidden layer, the learning rate,
                and the momentum factor. Our implementation was carried out
                using Python. You can find more detailed information about the
                project{" "}
                <a href="./Neural Network.pdf" target="_blank">
                  here
                </a>
                .
              </p>
            </div>
            <div className="image-container">
              <img src="../pictures/datasets.png" alt="Datasets for NN"></img>
              <figcaption>
                Datasets used. From UCI Machine learning Repo
              </figcaption>
            </div>
            <div className="image-container">
              <img
                src="../pictures/soybeanData.png"
                alt="Soybean dataset"
              ></img>
              <figcaption>Soybean data</figcaption>
            </div>
          </div>
        </section>

        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Game Stats</b>
              </h2>
              <p>
                This project was a personal passion endeavor that I undertook
                independently. I was interested in the abundance of freely
                accessible web APIs, and I selected one that provides player
                statistics for the game Rocket League. This RESTful API offers a
                plethera of data returned in JSON form, encompassing various
                statistics extracted from recent in-game tournaments. By
                aggregating and analyzing these statistics, I was able to
                identify the top-performing players in specific categories for
                each tournament. For example, players with the highest saves,
                shots, assists, and more.
              </p>
            </div>
            <div className="image-container">
              <img src="../pictures/OctaneGG.png" alt="OctaneGG api"></img>
              <figcaption>API used for project</figcaption>
            </div>
            <div className="image-container-code">
              <img src="../pictures/gameStatsCode.png" alt="Stats code"></img>
              <figcaption>Basic API call with params</figcaption>
            </div>
          </div>
        </section>
        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Wordle Solver</b>
              </h2>
              <p>
                I created this algorithm when the popular browser game wordle
                was at it's peak popularity. Using a dataset of over 5000 five
                letter words, the algorithm works by process of elimination. It
                gives you a random word to try, which you input into wordle, you
                then indicate which letters are in the correct position, which
                are part of the word but not correctly positioned, and finally,
                those that are not in the word at all. On average the solver
                gives you the correct word in approximately 4 guesses.
              </p>
            </div>
            <div className="image-container">
              <img src="../pictures/wordleImg.png" alt="Wordle"></img>
              <figcaption>Wordle</figcaption>
            </div>
            <div className="image-container-code">
              <img src="../pictures/wordleCode.png" alt="Wordle code"></img>
              <figcaption>Initialization / Main Loop</figcaption>
            </div>
          </div>
        </section>
      </FadeIn>
    </>
  );
};

export default Projects;
