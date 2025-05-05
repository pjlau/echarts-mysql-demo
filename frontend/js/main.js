// Initialize ECharts
const chart = echarts.init(document.getElementById('chart'));

// Chart configuration
const option = {
    title: {
        text: 'Product Sales'
    },
    tooltip: {},
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name: 'Sales',
        type: 'bar',
        data: []
    }]
};

// Fetch data from backend
fetch('http://localhost:8000/sales')
    .then(response => response.json())
    .then(data => {
        // Update chart data
        option.xAxis.data = data.map(item => item.product);
        option.series[0].data = data.map(item => item.sales);
        
        // Render chart
        chart.setOption(option);
    })
    .catch(error => console.error('Error fetching data:', error));

// Initial render
chart.setOption(option);