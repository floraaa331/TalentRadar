import React from 'react';
import SkillTags from './SkillTags';
import DemandGauge from './DemandGauge';
import SalaryCard from './SalaryCard';
import SkillChart from './SkillChart';

function ResultsDashboard({ result }) {
  return (
    <div className="results">
      <div className="results-header">
        <h2>Analysis Results</h2>
        <span className={`seniority-badge seniority-${result.seniority}`}>
          {result.seniority}
        </span>
      </div>

      <p className="summary">{result.summary}</p>

      <div className="results-grid">
        <DemandGauge score={result.market_demand_score} />
        <SalaryCard range={result.salary_range_rub} />
      </div>

      <div className="stack-tags">
        <h3>Tech Stack</h3>
        <div className="tags">
          {result.stack_tags.map((tag) => (
            <span key={tag} className="tag tag-stack">{tag}</span>
          ))}
        </div>
      </div>

      <SkillTags skills={result.skills} />
      <SkillChart skills={result.skills} />
    </div>
  );
}

export default ResultsDashboard;
