$(document).ready(function () {
    $('.article-item-title').click(function () {
        const url = $(this).attr('data');
        $(location).attr("href", url)
    })
})