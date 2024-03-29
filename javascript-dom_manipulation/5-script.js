const header = document.querySelector('header');

document.querySelector('#update_header').addEventListener('click', function (e) {
  header.innerHTML = 'New Header!!!';
});
