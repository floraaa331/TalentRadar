import React from 'react';

function Loading({ size = 'default', text = '' }) {
  return (
    <span className={`loading loading-${size}`}>
      <span className="spinner" />
      {text && <span className="loading-text">{text}</span>}
    </span>
  );
}

export default Loading;
