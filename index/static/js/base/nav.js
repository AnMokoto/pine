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
    let navbar_select = ['menu-bar-top', 'menu-bar-middle', 'menu-bar-bottom']

    $('.navbar-menu').click(function () {
        $(this).children().each(function (index) {
            if (navbar_menu) {
                $(this).removeClass(navbar_select[index])
            } else {
                $(this).addClass(navbar_select[index])
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