const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('.site-nav');

if (menuButton && navigation) {
  const menuLabel = menuButton.querySelector('.sr-only');

  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    navigation.classList.toggle('is-open', !isOpen);
    if (menuLabel) menuLabel.textContent = isOpen ? 'Open navigation' : 'Close navigation';
  });

  navigation.addEventListener('click', (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      menuButton.setAttribute('aria-expanded', 'false');
      navigation.classList.remove('is-open');
      if (menuLabel) menuLabel.textContent = 'Open navigation';
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 850) {
      menuButton.setAttribute('aria-expanded', 'false');
      navigation.classList.remove('is-open');
      if (menuLabel) menuLabel.textContent = 'Open navigation';
    }
  });
}

document.querySelectorAll('[data-current-year]').forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});
