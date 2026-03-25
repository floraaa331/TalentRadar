import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';

const CATEGORY_COLORS = {
  language: '#6366f1',
  framework: '#f59e0b',
  database: '#10b981',
  cloud: '#3b82f6',
  tool: '#8b5cf6',
  soft_skill: '#ec4899',
  methodology: '#14b8a6',
  other: '#94a3b8',
};

function SkillChart({ skills }) {
  const data = skills.map((s) => ({
    name: s.name,
    value: s.importance === 'must' ? 2 : 1,
    category: s.category,
  }));

  return (
    <section className="card chart-section">
      <h3>Skills Breakdown</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 10, right: 20, left: 0, bottom: 40 }}>
          <XAxis
            dataKey="name"
            angle={-35}
            textAnchor="end"
            tick={{ fontSize: 12, fill: 'var(--color-text-secondary)' }}
            interval={0}
          />
          <YAxis
            tick={{ fontSize: 12, fill: 'var(--color-text-secondary)' }}
            domain={[0, 2]}
            ticks={[1, 2]}
            tickFormatter={(v) => (v === 2 ? 'Must' : 'Nice')}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: 'var(--color-surface)',
              border: '1px solid var(--color-border)',
              borderRadius: '8px',
            }}
            formatter={(value, name, props) => [
              value === 2 ? 'Must have' : 'Nice to have',
              props.payload.category,
            ]}
          />
          <Bar dataKey="value" radius={[4, 4, 0, 0]}>
            {data.map((entry, i) => (
              <Cell key={i} fill={CATEGORY_COLORS[entry.category] || CATEGORY_COLORS.other} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
      <div className="chart-legend">
        {Object.entries(CATEGORY_COLORS).map(([cat, color]) => (
          <span key={cat} className="legend-item">
            <span className="legend-dot" style={{ backgroundColor: color }} />
            {cat.replace('_', ' ')}
          </span>
        ))}
      </div>
    </section>
  );
}

export default SkillChart;
