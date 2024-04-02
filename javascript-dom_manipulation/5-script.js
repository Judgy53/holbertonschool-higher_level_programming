// Cache header to avoid query on every click
const header = document.querySelector('header');

// Change header text when #update_header is clicked
document.querySelector('#update_header').addEventListener('click', () => {
  header.innerHTML = 'New Header!!!';
});
