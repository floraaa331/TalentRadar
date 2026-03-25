import React from 'react';
import { useTheme } from '../context/ThemeContext';

function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();

  return (
    <button className="theme-toggle" onClick={toggleTheme} aria-label="Toggle theme">
      {theme === 'dark' ? '\u2600' : '\u263E'}
    </button>
  );
}

export default ThemeToggle;
