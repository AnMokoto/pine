$(document).ready(function () {
    $('.article-item-title').click(function () {
        const url = $(this).attr('data');
        $(location).attr("href", url)
    })

    $('.article-item-title').hover(function () {
        $(this).animate({marginLeft: '5px'}, 'fast')
    }, function () {
        $(this).animate({marginLeft: '0px'}, 'fast')
    })
})