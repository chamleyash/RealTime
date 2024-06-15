'use strict';

/**
 * element toggle function
 */
const elemToggleFunc = function (elem) { elem.classList.toggle("active"); }

/**
 * navbar variables
 */
const navbar = document.querySelector("[data-nav]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const overlay = document.querySelector("[data-overlay]");

const navElemArr = [navOpenBtn, navCloseBtn, overlay];

for (let i = 0; i < navElemArr.length; i++) {
  navElemArr[i].addEventListener("click", function () {
    elemToggleFunc(navbar);
    elemToggleFunc(overlay);
    elemToggleFunc(document.body);
  });
}

/**
 * go top
 */
const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {
  if (window.scrollY >= 800) {
    goTopBtn.classList.add("active");
  } else {
    goTopBtn.classList.remove("active");
  }
});

/**
 * Modal handling
 */
var loginModal = document.getElementById("loginModal");
var registerModal = document.getElementById("registerModal");

// Get the button that opens the login modal
var loginBtn = document.querySelector(".btn-sign_in");

// Get the <span> elements that close the modals
var closeLogin = loginModal.getElementsByClassName("close")[0];
var closeRegister = registerModal.getElementsByClassName("close")[0];

// When the user clicks the button, open the login modal 
loginBtn.onclick = function() {
  loginModal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
closeLogin.onclick = function() {
  loginModal.style.display = "none";
}

closeRegister.onclick = function() {
  registerModal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == loginModal) {
    loginModal.style.display = "none";
  }
  if (event.target == registerModal) {
    registerModal.style.display = "none";
  }
}

// Handle new user registration link
var registerLink = document.getElementById("registerLink");

registerLink.onclick = function(event) {
  event.preventDefault();
  loginModal.style.display = "none";
  registerModal.style.display = "block";
}
