import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroContent}>
          <Heading as="h1" className={clsx('hero__title', styles.heroTitle)}>
            Master Humanoid Robotics with AI
          </Heading>
          <p className={clsx('hero__subtitle', styles.heroSubtitle)}>
            A comprehensive, interactive textbook covering Physical AI, locomotion,
            manipulation, and sensing for next-generation humanoid robots
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/docs/book-chapters/chapter_01_introduction">
              Start Learning 🚀
            </Link>
            <Link
              className={clsx('button button--outline button--secondary button--lg', styles.buttonSecondary)}
              to="/docs/book-chapters/chapter_01_introduction/code-samples">
              View Code Examples 💻
            </Link>
          </div>
          <div className={styles.heroStats}>
            <div className={styles.stat}>
              <div className={styles.statNumber}>4</div>
              <div className={styles.statLabel}>Comprehensive Chapters</div>
            </div>
            <div className={styles.stat}>
              <div className={styles.statNumber}>40+</div>
              <div className={styles.statLabel}>Exercises & Problems</div>
            </div>
            <div className={styles.stat}>
              <div className={styles.statNumber}>12</div>
              <div className={styles.statLabel}>AI Learning Assistants</div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

function ChapterOverview(): ReactNode {
  const chapters = [
    {
      number: 1,
      title: 'Introduction to Physical AI',
      description: 'Explore the foundations of Physical AI and humanoid robotics, including perception, cognition, and control theory.',
      link: '/docs/book-chapters/chapter_01_introduction',
      topics: ['Physical AI Basics', 'Theoretical Foundations', 'Real-World Examples']
    },
    {
      number: 2,
      title: 'Robot Locomotion',
      description: 'Learn about kinematics, dynamics, and gait generation for wheeled, bipedal, and quadrupedal systems.',
      link: '/docs/book-chapters/chapter_02_robot_locomotion',
      topics: ['Kinematics & Dynamics', 'ZMP & Balance', 'Gait Planning']
    },
    {
      number: 3,
      title: 'Robot Manipulation',
      description: 'Master grasping theory, motion planning algorithms, and control systems for robotic manipulation.',
      link: '/docs/book-chapters/chapter_03_robot_manipulation',
      topics: ['Grasping & Force Closure', 'Motion Planning', 'Control Systems']
    },
    {
      number: 4,
      title: 'Robot Sensing',
      description: 'Understand proprioceptive and exteroceptive sensors, and learn sensor fusion techniques for robust perception.',
      link: '/docs/book-chapters/chapter_04_robot_sensing',
      topics: ['Sensor Types', 'Sensor Fusion', 'State Estimation']
    },
  ];

  return (
    <section className={styles.chapterSection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          What You'll Learn
        </Heading>
        <p className={styles.sectionSubtitle}>
          Four comprehensive chapters covering the essential topics in humanoid robotics
        </p>
        <div className={styles.chapterGrid}>
          {chapters.map((chapter) => (
            <Link key={chapter.number} to={chapter.link} className={styles.chapterCard}>
              <div className={styles.chapterNumber}>Chapter {chapter.number}</div>
              <Heading as="h3" className={styles.chapterTitle}>{chapter.title}</Heading>
              <p className={styles.chapterDescription}>{chapter.description}</p>
              <ul className={styles.topicList}>
                {chapter.topics.map((topic, idx) => (
                  <li key={idx}>✓ {topic}</li>
                ))}
              </ul>
              <div className={styles.chapterLink}>
                Read Chapter →
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Master Humanoid Robotics with AI"
      description="A comprehensive, interactive textbook covering Physical AI, locomotion, manipulation, and sensing for humanoid robots. Includes AI-powered learning assistants and simulation-ready code examples.">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <ChapterOverview />
      </main>
    </Layout>
  );
}
