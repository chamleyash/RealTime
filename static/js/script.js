document.addEventListener('DOMContentLoaded', function() {
  'use strict';

  const elemToggleFunc = function (elem) {
    if (elem) {
      elem.classList.toggle("active");
    }
  }

  const navbar = document.querySelector("[data-nav]");
  const navOpenBtn = document.querySelector("[data-nav-open-btn]");
  const navCloseBtn = document.querySelector("[data-nav-close-btn]");
  const overlay = document.querySelector("[data-overlay]");

  const navElemArr = [navOpenBtn, navCloseBtn, overlay];

  navElemArr.forEach(elem => {
    if (elem) {
      elem.addEventListener("click", function () {
        elemToggleFunc(navbar);
        elemToggleFunc(overlay);
        elemToggleFunc(document.body);
      });
    }
  });

  const goTopBtn = document.querySelector("[data-go-top]");

  window.addEventListener("scroll", function () {
    if (window.scrollY >= 800) {
      goTopBtn.classList.add("active");
    } else {
      goTopBtn.classList.remove("active");
    }
  });

  const loginModal = document.getElementById("loginModal");
  const loginBtn = document.querySelector(".btn-sign_in");
  const closeLogin = loginModal ? loginModal.getElementsByClassName("icon-close")[0] : null;

  if (loginBtn) {
    loginBtn.onclick = function() {
      if (loginModal) loginModal.style.display = "block";
    }
  }

  if (closeLogin) {
    closeLogin.onclick = function() {
      if (loginModal) loginModal.style.display = "none";
    }
  }

  window.onclick = function(event) {
    if (event.target == loginModal) {
      loginModal.style.display = "none";
    }
  }

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  const joinBtn = document.querySelector('.join-btn');
  if (joinBtn) {
    joinBtn.addEventListener('click', function() {
      window.location.href = 'Tournament.html';
    });
  }
});
