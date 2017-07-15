var isFixed = false;
var $navbar = $('.navbar');
var $window = $(window);
var $body = $('body');
$window.scroll(function() {
    if(!window.matchMedia('(max-width: 767px)').matches){
        if ($window.scrollTop() >= 195) {
            if (!isFixed) {
                $navbar.addClass('navbar-fixed-top');
                $navbar.css("border-top", "4px solid red");
                $body.css("padding-top", "73px");
                isFixed = true;
            }} else {if (isFixed) {
                $navbar.removeClass('navbar-fixed-top');
                $navbar.css("border-top", "none");
                $body.css("padding-top", "0px");
                isFixed = false;
            }
        }
    }
}).trigger('scroll');


