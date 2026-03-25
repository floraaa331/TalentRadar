import React from 'react';

function formatRub(n) {
  return new Intl.NumberFormat('ru-RU', { style: 'currency', currency: 'RUB', maximumFractionDigits: 0 }).format(n);
}

function SalaryCard({ range }) {
  return (
    <div className="card salary-card">
      <h3>Salary Estimate</h3>
      <div className="salary-range">
        <div className="salary-value">
          <span className="salary-label">Min</span>
          <span className="salary-amount">{formatRub(range.min)}</span>
        </div>
        <span className="salary-divider">&mdash;</span>
        <div className="salary-value">
          <span className="salary-label">Max</span>
          <span className="salary-amount">{formatRub(range.max)}</span>
        </div>
      </div>
      <span className="salary-note">Monthly, gross (RUB)</span>
    </div>
  );
}

export default SalaryCard;
