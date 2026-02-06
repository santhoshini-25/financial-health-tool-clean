import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function Dashboard({ insights, data }) {  // Ensure 'data' is in props
  const safeData = data || { revenue: 0, expenses: 0 };
  const profit = (safeData.revenue - safeData.expenses) || 0;

  const chartData = {
    labels: ['Revenue', 'Expenses', 'Profit'],
    datasets: [{
      label: 'Financial Metrics',
      data: [safeData.revenue, safeData.expenses, profit],
      backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
      borderColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
      borderWidth: 1,
    }],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Financial Health Overview' },
    },
  };

  const hasData = safeData.revenue > 0 || safeData.expenses > 0;

  return (
    <div>
      <h2>Financial Insights</h2>
      <p>{insights || 'Upload data to see AI insights here.'}</p>
      {hasData ? (
        <Bar data={chartData} options={options} />
      ) : (
        <p>No data available for chart. Please upload a file with revenue/expenses.</p>
      )}
    </div>
  );
}

export default Dashboard;