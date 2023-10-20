import "./About.css";
import FadeIn from "react-fade-in/lib/FadeIn";

const About = () => {
  return (
    <>
      <FadeIn>
        <div className="about-header">
          <h1>
            <b>About Me</b>
          </h1>
          <h3>My Background and Interests</h3>
        </div>
        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Skiing</b>
              </h2>
              <p>
                Living near Whitefish, Montana, means living close to Big
                Mountain. My dad taught me how to ski at a very young age, and
                I've been skiing most winters since. There's nothing better than
                waking up early on a Saturday, gearing up, and driving to the
                mountain on a crisp winter day. Upon arrival, the mountain
                offers incredible scenic beauty and a variety of routes to keep
                us entertained all day.
              </p>
            </div>
            <div className="image-container">
              <img
                src="../pictures/SkiingPic.jpg"
                alt="Skiing with family"
              ></img>
            </div>
            <div className="image-container">
              <img src="../pictures/BigMountain.jpg" alt="Big Mountain"></img>
            </div>
          </div>
        </section>
        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Alaskan Hiking</b>
              </h2>
              <p>
                My sister lives in Alaska, and I had the opportunity to visit
                her and her fiancé last summer. During the trip, I was able to
                visit Seward, Alaska, where the Resurrection Bay fjord meets the
                mountains creating a stunning view (as seen on the right). There
                are seemingly endless hikes and outdoor activities to enjoy
                during the summer, which, combined with the picturesque
                landscapes, made for the best summer vacation.
              </p>
            </div>
            <div className="image-container">
              <img src="../pictures/Seward.jpg" alt="Seward, Alaska"></img>
              <div className="image">
                <img src="../pictures/ReidLakesTop.jpg" alt="Reid Lakes"></img>
              </div>
            </div>
            <div className="image-container">
              <img src="../pictures/ChampTrailHike.jpg" alt="Champ Trail"></img>
              <div className="image">
                <img src="../pictures/ReidLakes.jpg" alt="Reid Lakes"></img>
              </div>
            </div>
          </div>
        </section>
        <section className="about-section shadow-lg p-3 mb-5 bg-aqua rounded">
          <div className="section-content">
            <div className="text">
              <h2>
                <b>Goldens</b>
              </h2>
              <p>
                These dogs are among the most comically clumsy creatures around.
                Despite their penchant for mischief, they undeniably add a touch
                of excitement and joy to life. Although both of these retrievers
                look alike, they are actually two completely different bundles
                of joy.
              </p>
            </div>
            <div className="image-container-dog">
              <img src="../pictures/BeauxBall.jpg" alt="Golden"></img>
            </div>
            <div className="image-container-dog">
              <img
                src="../pictures/HoldingYukla.jpg"
                alt="MeHoldingYukla"
              ></img>
            </div>
            <div className="image-container-dog">
              <img src="../pictures/Yukla.jpg" alt="Golden"></img>
            </div>
          </div>
        </section>
      </FadeIn>
    </>
  );
};

export default About;
