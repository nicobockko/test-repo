# https://echarts.apache.org/examples/en/editor.html?c=wind-barb


$.getJSON(
    ROOT_PATH + '/data/assets/data/wind-barb-hobart.json',
    function(rawData)
{
    const
directionMap = {};
// prettier - ignore
['W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE', 'E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW'].forEach(
    function(name, index)
{
    directionMap[name] = Math.PI / 8 * index;
});
const
data = rawData.data.map(function(entry)
{
return [entry.time, entry.windSpeed, entry.R, entry.waveHeight];
});
const
weatherData = rawData.forecast.map(function(entry)
{
return [
    entry.localDate,
    0,

    entry.minTemp,
    entry.maxTemp
];
});
const
dims = {
    time: 0,
    windSpeed: 1,
    R: 2,
    waveHeight: 3,
    weatherIcon: 2,
    minTemp: 3,
    maxTemp: 4
};
const
arrowSize = 18;
const
renderArrow = function(param, api)
{
    const
point = api.coord([
    api.value(dims.time),
    api.value(dims.windSpeed)
]);
return {
    type: 'path',
    shape: {
        pathData: 'M31 16l-15-15v9h-26v12h26v9z',
        x: -arrowSize / 2,
        y: -arrowSize / 2,
        width: arrowSize,
        height: arrowSize
    },
    rotation: directionMap[api.value(dims.R)],
    position: point,
    style: api.style({
        stroke: '#555',
        lineWidth: 1
    })
};
};

option = {
xAxis: {
    type: 'time',
    maxInterval: 3600 * 1000 * 24,
    splitLine: {
        lineStyle: {
            color: '#ddd'
        }
    }
},
yAxis: [
    {
    },
    {
    },
    {
    }
],
visualMap: {
               type: 'piecewise',
           // show: false,
orient: 'horizontal',
left: 'center',
bottom: 10,
pieces: [
    {
        gte: 17,
        color: '#18BF12',
        label: '大风（>=17节）'
    },
    {
        gte: 11,
        lt: 17,
        color: '#f4e9a3',
        label: '中风（11  ~ 17 节）'
    },
    {
        lt: 11,
        color: '#D33C3E',
        label: '微风（小于 11 节）'
    }
],
seriesIndex: 1,
dimension: 1
},
series: [
    {
        type: 'line',
        yAxisIndex: 1,
        showSymbol: false,
        emphasis: {
            scale: false
        },
        encode: {
            x: dims.time,
            y: dims.waveHeight
        },
        data: data,
        z: 2
    },
    {
        type: 'custom',
        renderItem: renderArrow,
        encode: {
            x: dims.time,
            y: dims.windSpeed
        },
        data: data,
        z: 10
    },

]
};
myChart.setOption(option);
}
);