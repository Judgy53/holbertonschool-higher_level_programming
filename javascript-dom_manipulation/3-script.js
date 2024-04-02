// Cache header element to avoid query on every click
const headerElem = document.querySelector('header');

// Toggle header color between red and green when #toggle_header is clicked
document.querySelector('#toggle_header').addEventListener('click', () => {
  headerElem.classList.toggle('red');
  headerElem.classList.toggle('green');
});
