$(document).ready(() => {


    let navText = ["<i class='bx bx-chevron-left'></i>","<i class='bx bx-chevron-right'></i>"]
    $('#movie-carousel').owlCarousel({
    item: 1,
    loop:true,
    nav: true,
    dots: false,
    margin: 10,
    navText: navText
    })

    
})

