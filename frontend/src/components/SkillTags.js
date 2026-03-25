import React from 'react';

function SkillTags({ skills }) {
  const must = skills.filter((s) => s.importance === 'must');
  const nice = skills.filter((s) => s.importance === 'nice');

  return (
    <section className="card skill-tags-section">
      <h3>Required Skills</h3>
      <div className="tags">
        {must.map((s) => (
          <span key={s.name} className="tag tag-must" title={s.category}>
            {s.name}
          </span>
        ))}
      </div>
      {nice.length > 0 && (
        <>
          <h3 style={{ marginTop: '1rem' }}>Nice to Have</h3>
          <div className="tags">
            {nice.map((s) => (
              <span key={s.name} className="tag tag-nice" title={s.category}>
                {s.name}
              </span>
            ))}
          </div>
        </>
      )}
    </section>
  );
}

export default SkillTags;
