document.querySelector('#toggle_header').addEventListener('click', function (e) {
  const headerClassList = document.querySelector('header').classList;
  headerClassList.toggle('red');
  headerClassList.toggle('green');
});
