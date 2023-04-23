const productContainers = [...document.querySelectorAll('.new_product-container')];
const nextBtn = [...document.querySelectorAll('.next-btn')];
const predBtn = [...document.querySelectorAll('.pred-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;


    nextBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })
    predBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})