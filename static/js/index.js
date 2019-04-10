var dd = false;

function dropDown() {
    if (dd === false) {
        $(".fa-bars").css({
            transform: 'rotate(90deg)',
            transition: '0.5s ease-in-out'
        });
        $(".menu").css({
            display: 'block',
            transform: 'translateY(0)',
            transition: '1s ease-in-out',
        });
        dd = true;
    } else {
        $(".fa-bars").css("transform", "rotate(0deg)");
        $(".menu").css("display", "none");
        dd = false;
    }

}

$(".gallery img").click(function (e) {
    img = $(e.target).attr("src");
    $("body").append('<div class="overlay" onclick="Rem(this)"><img src=""></div>');
    $(".overlay img").attr("src", img)
});

function Rem(e) {
    console.log("Test")
    $(".overlay").remove()
}