import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api',
  timeout: 60000,
});

export async function analyzeJob(jobDescription) {
  const { data } = await api.post('/analysis/', { job_description: jobDescription });
  return data;
}

export async function getHistory(limit = 10) {
  const { data } = await api.get('/history/', { params: { limit } });
  return data;
}

export async function getStats() {
  const { data } = await api.get('/history/stats');
  return data;
}

export default api;
