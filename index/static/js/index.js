// import Chart from 'Chart.min.js';
// $(document).ready(new function () {
//     $.get('{% url %}')
// })



function onEjsTemplate(url, cb) {
    onJsFile(url, cb, 'html')
}

function onJsApi(url, cb) {
    onJsFile(url, cb, 'json')
}

function onJsFile(url, cb, dataType) {
    $.ajax({
        url: url,
        type: 'GET',
        dataType: dataType,
        success: cb,
        error: cb
    })
}


function startFull(dom) {
    dom.fullpage({
        menu: null,
        // anchors: ['page1', 'page2', 'page3'],//#id
        sectionsColor: ['#bfda00', '#2ebe21', '#2C3E50', '#51bec4'],//每个section的背景色
        loopTop: true,
        loopBottom: true,
        easing: 'easeInOutCubic',
        scrollingSpeed: 500,
        css3: true,

        navigation: {//标签
            'textColor': '#000',
            'bulletsColor': '#000',
            'position': 'right',
            'tooltips': ['section1', 'section2', 'section3', 'section4'],
        },
        sectionSelector: '.section',
        lazyLoading: true,

        onLeave: function (index, nextIndex, direction) {
            if (nextIndex === 1 || direction === 'up') {
                // $('nav').fadeIn();
                $('nav').animate({
                    top: '0px',
                    opacity: 1,
                }, 500, 'easeInOutCubic');
            } else {
                // $('nav').fadeOut();
                $('nav').animate({
                    top: '-200px',
                    opacity: 0.5,
                }, 500, 'easeInOutCubic');
            }
        }
    });
}


$(document).ready(function () {
    window.startFull($('#content'))
});

//
