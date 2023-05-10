// Popup
let popup = document.querySelector('.popup-nav');
let openPopupButton = document.getElementById('popup-nav_open');
let closePopupButton = document.getElementById('popup-nav_close');
let darkness = document.getElementById('darkness');
let popupDark = document.querySelector('.popup_dark')
let closePopups1 = document.getElementById('popup-close1')
let closePopups2 = document.getElementById('popup-close2')
let closePopups3 = document.getElementById('popup-close3')
let closePopups4 = document.getElementById('popup-close4')
let closePopups5 = document.getElementById('popup-close5')
let closePopups6 = document.getElementById('popup-close6')
let closePopups7 = document.getElementById('popup-close7')
let closePopups8 = document.getElementById('popup-close8')

let popupOne = document.querySelector('.popup-1')
let courseOne = document.getElementById('course-1')

let popupTwo = document.querySelector('.popup-2')
let courseTwo = document.getElementById('course-2')

let popupThree = document.querySelector('.popup-3')
let courseThree = document.getElementById('course-3')

let popupFour = document.querySelector('.popup-4')
let courseFour = document.getElementById('course-4')

let popupFive = document.querySelector('.popup-5')
let courseFive = document.getElementById('course-5')

let popupSix = document.querySelector('.popup-6')
let courseSix = document.getElementById('course-6')

let popupSeven = document.querySelector('.popup-7')
let courseSeven = document.getElementById('course-7')

let popupEight = document.querySelector('.popup-8')
let courseEight = document.getElementById('course-8')



// Offers
let offer = document.getElementById('offers-img');

// Popup events
openPopupButton.addEventListener('click', () => {
  popup.classList.add('popup-nav_active')
})

closePopupButton.addEventListener('click', () => {
  popup.classList.remove('popup-nav_active')
})

// Smooth links
const smoothLinks = document.querySelectorAll('a[href^="#"]');
for (let smoothLink of smoothLinks) {
  smoothLink.addEventListener('click', function (e) {
    e.preventDefault();
    const id = smoothLink.getAttribute('href');

    document.querySelector(id).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
    popup.classList.remove('popup-nav_active')
  });
}

// Scroll anim
function onEntry(entry) {
  entry.forEach(change => {
    if (change.isIntersecting) {
      change.target.classList.add('element-show');
    }
  });
}
let options = { threshold: [0], rootMargin: '190px', };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');
for (let elm of elements) {
  observer.observe(elm);
}

document.addEventListener("DOMContentLoaded", () => {
  darkness.classList.add('darkness_none')
})

courseOne.addEventListener('click', () => {
  popupOne.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseTwo.addEventListener('click', () => {
  popupTwo.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseThree.addEventListener('click', () => {
  popupThree.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseFour.addEventListener('click', () => {
  popupFour.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseFive.addEventListener('click', () => {
  popupFive.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseSix.addEventListener('click', () => {
  popupSix.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseSeven.addEventListener('click', () => {
  popupSeven.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})

courseEight.addEventListener('click', () => {
  popupEight.classList.add('popup_active')
  popupDark.classList.add('popup_active')
})
// 
// closePopups.forEach((item) => {
//   item.addEventListener('click', () => {
//     popupOne.classList.remove('popup_active')
//     popupDark.classList.remove('popup_active')
//     
//     popupTwo.classList.remove('popup_active')
//     popupThree.classList.remove('popup_active')
//     popupFour.classList.remove('popup_active')
//     popupFive.classList.remove('popup_active')
//     popupSix.classList.remove('popup_active')
//     popupSeven.classList.remove('popup_active')
//     popupEight.classList.remove('popup_active')
//   })
// })

closePopups1.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupOne.classList.remove('popup_active')
})

closePopups2.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupTwo.classList.remove('popup_active')
})

closePopups3.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupThree.classList.remove('popup_active')
})

closePopups4.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupFour.classList.remove('popup_active')
})

closePopups5.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupFive.classList.remove('popup_active')
})

closePopups6.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupSix.classList.remove('popup_active')
})

closePopups7.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupSeven.classList.remove('popup_active')
})

closePopups8.addEventListener('click', () => {
  popupDark.classList.remove('popup_active')
  popupEight.classList.remove('popup_active')
})