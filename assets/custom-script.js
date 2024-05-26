//new Swiper('.swiper-container', {
//  direction: 'vertical', // 수직 슬라이드
//  autoplay: true, // 자동 재생 여부
//  loop: true // 반복 재생 여부
//});

console.log('ggg');
//(function() { // DON'T EDIT BELOW THIS LINE
//var d = document, s = d.createElement('script');
//s.src = 'https://dash-test.disqus.com/embed.js';
//s.setAttribute('data-timestamp', +new Date());
//(d.head || d.body).appendChild(s);
//})();

console.log('ggg');


var hh = document.getElementById('myecharts');
var echart = echarts.getInstanceByDom(hh);
//getInstanceByDom
//var echart = echarts.init(hh);

window.addEventListener('resize', function() {
    if (echart) {

        echart.resize();
    }
});


console.log('꾸꾸');


