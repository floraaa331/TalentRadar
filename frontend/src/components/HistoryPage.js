import React, { useEffect, useState } from 'react';
import { getHistory, getStats } from '../api';
import { useApi } from '../hooks/useApi';
import Loading from './Loading';
import ResultsDashboard from './ResultsDashboard';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const PIE_COLORS = ['#6366f1', '#f59e0b', '#10b981'];

function HistoryPage() {
  const { data: history, loading: histLoading, error: histError, execute: loadHistory } = useApi(getHistory);
  const { data: stats, loading: statsLoading, execute: loadStats } = useApi(getStats);
  const [expanded, setExpanded] = useState(null);

  useEffect(() => {
    loadHistory(10);
    loadStats();
  }, []);

  if (histLoading && !history) {
    return <div className="page center"><Loading text="Loading history..." /></div>;
  }

  if (histError) {
    return <div className="page"><div className="error-banner">{histError}</div></div>;
  }

  const seniorityData = stats?.seniority_distribution
    ? Object.entries(stats.seniority_distribution).map(([name, value]) => ({ name, value }))
    : [];

  return (
    <div className="page">
      {stats && (
        <div className="stats-grid">
          <div className="card stat-card">
            <h3>Total Analyses</h3>
            <span className="stat-number">{stats.total_analyses}</span>
          </div>

          {stats.top_skills?.length > 0 && (
            <div className="card stat-card stat-card-wide">
              <h3>Top Skills</h3>
              <ResponsiveContainer width="100%" height={200}>
                <BarChart data={stats.top_skills.slice(0, 10)}>
                  <XAxis dataKey="name" tick={{ fontSize: 11, fill: 'var(--color-text-secondary)' }} angle={-30} textAnchor="end" interval={0} />
                  <YAxis tick={{ fontSize: 11, fill: 'var(--color-text-secondary)' }} />
                  <Tooltip contentStyle={{ backgroundColor: 'var(--color-surface)', border: '1px solid var(--color-border)', borderRadius: '8px' }} />
                  <Bar dataKey="count" fill="#6366f1" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          )}

          {seniorityData.length > 0 && (
            <div className="card stat-card">
              <h3>Seniority Split</h3>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie data={seniorityData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={70} label={({ name, value }) => `${name} (${value})`}>
                    {seniorityData.map((_, i) => (
                      <Cell key={i} fill={PIE_COLORS[i % PIE_COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          )}
        </div>
      )}

      <h2 style={{ marginTop: '2rem' }}>Recent Analyses</h2>
      {(!history || history.length === 0) ? (
        <p className="empty-state">No analyses yet. Go analyze some job descriptions!</p>
      ) : (
        <div className="history-list">
          {history.map((item) => (
            <div key={item.id} className="card history-item">
              <div
                className="history-item-header"
                onClick={() => setExpanded(expanded === item.id ? null : item.id)}
              >
                <div className="history-meta">
                  <span className={`seniority-badge seniority-${item.seniority}`}>{item.seniority}</span>
                  <span className="history-score">Demand: {item.market_demand_score}/10</span>
                  <span className="history-date">{new Date(item.created_at).toLocaleString()}</span>
                </div>
                <p className="history-preview">{item.job_description.slice(0, 120)}...</p>
                <span className="expand-icon">{expanded === item.id ? '\u25B2' : '\u25BC'}</span>
              </div>
              {expanded === item.id && <ResultsDashboard result={item} />}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default HistoryPage;
