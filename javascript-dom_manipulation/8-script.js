function fetchAndDisplayHello () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error while fetching hello message');
      }

      response.json()
        .then((json) => {
          document.querySelector('#hello').innerHTML = json.hello;
        });
    });
}

document.addEventListener('DOMContentLoaded', fetchAndDisplayHello);
