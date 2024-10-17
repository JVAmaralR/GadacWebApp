const slider = document.querySelectorAll('.slider');
const btnPrev = document.getElementById('prev-button');
const btnNext = document.getElementById('next-button');

let currentslide = 0;

function hideslider() {
    slider.forEach(iten => iten.classList.remove('on'))
}

function showslider() {
    slider[currentslide].classList.add('on')
}

btnNext.addEventListener('click', () => {
    hideslider();
    currentslide = (currentslide + 1) % slider.length; // Avança para o próximo slide, voltando ao início se necessário
    showslider();
});

btnPrev.addEventListener('click', () => {
    hideslider();
    currentslide = (currentslide - 1 + slider.length) % slider.length; // Volta para o slide anterior, ou para o último se necessário
    showslider();
});

setInterval(() => {
    hideslider();
    currentslide = (currentslide + 1) % slider.length; // Avança para o próximo slide
    showslider();
}, 10000);