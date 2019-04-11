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


//Gallery

var arr = [];
for (var i = 0; i < $(".gallery img").length; i++) {
    arr[i] = $(".gallery img")[i];
}


$(".gallery img").click(function (e) {
    $("body").append('<div class="overlay"><img src="" number=""><div class="controls"><i class="fas fa-arrow-left" onclick="Prev()"></i><i class="fas fa-times" onclick="Close()"></i><i class="fas fa-arrow-right" onclick="Next()"></i></div></div>');
    change($(e.target).attr("number"))
});

function Prev() {
    num =  parseInt($(".overlay img").attr("number"),10)
    if(num === 0){
        change( arr.length - 1)
    }else{
        change( num - 1)
    }
}

function Next() {
    num =  parseInt($(".overlay img").attr("number"),10)
    if(num === arr.length - 1){
        change( 0)
    }else{
        change( num + 1)
    }
}

function Close() {
    $(".overlay").remove()
}

function change(id) {
    adress = $(arr[id]).attr("src")
    $(".overlay img").attr("src", adress).attr("number", id)
}