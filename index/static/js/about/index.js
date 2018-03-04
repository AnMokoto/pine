$(document).ready(function () {


    function OnResize() {

        $(document.body).css({
            "width": $(window).width(),
            "height": $(window).height(),
        });

        $('#content .content-first').css({
            "height": $(document.body).height(),
        })
    }

    $(window).resize(() => OnResize())

    OnResize()

})

function createChartLayout(name, labels, data, colors) {
    const ctx = document.getElementById(name);
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors,
                borderColor: "transparent",
                hoverBorderColor: "transparent"
            }]
        },
        options: _options(name)
    })
}

function _options(name) {
    return {
        legend: {
            position: 'bottom',
            display: 0 //if `True` show the labels or hidden.
        },
        responsive: true,
        title: {
            display: true,
            text: name.toLocaleUpperCase()
        },
        animation: {
            animateScale: true,
            animateRotate: true
        },
    }
}

function colors() {
    let color = [];
    while (color.length < 6) {
        let hex = (parseInt(Math.random() * 16)).toString(16);
        color.push(hex)
    }
    return color.join("").toUpperCase();
}