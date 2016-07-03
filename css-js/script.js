jQuery(document).ready(function () {
    var windowHeight = jQuery(window).height();
    var windowScrollPosTop = jQuery(window).scrollTop();
    var windowScrollPosBottom = windowHeight + windowScrollPosTop;


    var navOffSet = jQuery("nav").offset().top;
    jQuery("nav").wrap('<div class="place-holder"></div');
    jQuery(".place-holder").height(jQuery("nav").outerHeight());

    jQuery(window).scroll(function () {
        //var scrollPosition = jQuery(window).scrollTop();

        if (windowScrollPosTop >= navOffSet) { //windowScrollPosTop is declared on top
            //alert('matched');
            jQuery("nav").addClass("fixed");
        } else {
            jQuery("nav").removeClass("fixed");
        }
    });
});
