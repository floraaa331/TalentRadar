import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import ThemeToggle from './ThemeToggle';

function Header() {
  const location = useLocation();

  return (
    <header className="header">
      <div className="header-inner">
        <Link to="/" className="logo">
          <span className="logo-icon">&#9678;</span>
          <span className="logo-text">TalentRadar</span>
        </Link>
        <nav className="nav">
          <Link to="/" className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}>
            Analyze
          </Link>
          <Link to="/history" className={`nav-link ${location.pathname === '/history' ? 'active' : ''}`}>
            History
          </Link>
          <ThemeToggle />
        </nav>
      </div>
    </header>
  );
}

export default Header;
