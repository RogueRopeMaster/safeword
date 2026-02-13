(function () {
  var button = document.getElementById("menu-toggle");
  var menu = document.getElementById("site-menu");

  if (!button || !menu) {
    return;
  }

  var isOpen = false;

  function setMenuState(nextState) {
    isOpen = !!nextState;
    button.setAttribute("aria-expanded", String(isOpen));
    menu.classList.toggle("is-open", isOpen);
  }

  function closeMenuOnDesktop() {
    if (window.innerWidth > 768) {
      setMenuState(false);
    }
  }

  button.addEventListener("click", function () {
    setMenuState(!isOpen);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      setMenuState(false);
      button.focus();
    }
  });

  document.addEventListener("click", function (event) {
    if (!isOpen) {
      return;
    }

    var clickedInsideMenu = menu.contains(event.target) || button.contains(event.target);
    if (!clickedInsideMenu) {
      setMenuState(false);
    }
  });

  window.addEventListener("resize", closeMenuOnDesktop);
})();
