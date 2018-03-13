$(document).ready(function () {
    let scroll = $(window).height();
    let nav_show = false;
    $(window).bind('scroll', function () {
        const top = $(document).scrollTop()
        if (top >= scroll && !nav_show) {
            $('.navbar-customize').css({
                'position': 'fixed'
            });
            $('.navbar-customize').fadeIn()
            nav_show = true
        } else if (top < scroll && nav_show) {
            $('.navbar-customize').fadeOut()
            $('.navbar-customize').css({
                'position': 'absolute'
            });
            nav_show = false;
            if (navbar_menu)
                $('.navbar-menu').click()
        }
    })

    $('.feather-home').click(function () {
        $(window).scrollTop(0)
    })

    let navbar_menu = false;

    $('.navbar-menu').click(function () {
        $(this).children().each(function (index) {
            switch (index) {
                case 0:
                    $(this).css({
                        'transform': navbar_menu ? 'rotate(0deg)' : 'rotate(45deg)',
                    })
                    break;
                case 1:
                    $(this).css({
                        'opacity': navbar_menu ? 1 : 0,
                    })
                    break;
                case 2:
                    $(this).css({
                        'transform': navbar_menu ? 'rotate(0deg)' : 'rotate(-45deg)',
                    })

            }
        })
        navbar_menu = !navbar_menu;

        if (navbar_menu) {
            $('.navbar-box').fadeIn(measureNavbarBoxItem())
        } else {
            $('.navbar-box').fadeOut()
        }

    }).hover(function () {
        $(this).children().each(function () {
            $(this).css({
                'background-color': 'orange'
            })
        })
    }, function () {
        $(this).children().each(function () {
            $(this).css({
                'background-color': ''
            })
        })
    })

    $('.navbar-box-content').delegate('a', 'click', function () {
        if (navbar_menu)
            $('.navbar-menu').click()
    })
    $('.navbar-box').click(function () {
        $('.navbar-menu').click()
    })

    function measureNavbarBoxItem() {
        const width = $('.navbar-box').width() - 100;
        const childW = width / 5 - 5;
        $('.navbar-box-content-item').css({
            width: childW,
            height: childW * (10 / 9)
        })
    }

    $(window).resize(() => measureNavbarBoxItem())

})