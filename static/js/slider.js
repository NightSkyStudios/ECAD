var Slide = 1;
var slides = $(".slider img");
PlaceDots();

function PlaceDots() {
    var i = 0;
    for (i; i < slides.length; i++) {
        $(".dots").append('<div class="dot"></div>')
    }
}

var dots = $(".dot");

progress(Slide);

function progress(n) {
    $(slides[Slide-2]).css("display","none");
    if (n > slides.length) {
        Slide = 1;
        for(var i=0;i<dots.length;i++){
            $(dots[i]).removeClass("active");
        }
    }
    $(slides[Slide-1]).css("display","block");
    setTimeout(function () {
        $(dots[Slide - 1]).addClass("active");
        Slide++
    },10);
}
setInterval(function () {
    progress(Slide)
}, 10 + 5000);