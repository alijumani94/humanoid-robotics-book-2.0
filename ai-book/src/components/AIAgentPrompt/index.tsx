import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

interface AIAgentPromptProps {
  type: 'explainer' | 'quiz' | 'lab-assistant';
  children: React.ReactNode;
}

const AIAgentPrompt: React.FC<AIAgentPromptProps> = ({ type, children }) => {
  const icon = {
    explainer: '💡',
    quiz: '🤔',
    'lab-assistant': '🧑‍🔬',
  }[type];

  const title = {
    explainer: 'Explainer Agent',
    quiz: 'Quiz Agent',
    'lab-assistant': 'Lab Assistant',
  }[type];

  return (
    <div className={clsx(styles.aiAgentPrompt, styles[type])}>
      <div className={styles.header}>
        <span className={styles.icon}>{icon}</span>
        <span className={styles.title}>{title}</span>
      </div>
      <div className={styles.content}>{children}</div>
    </div>
  );
};

export default AIAgentPrompt;
