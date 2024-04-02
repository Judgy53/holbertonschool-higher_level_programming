function fetchAndDisplayHello (langSelectElem, outputElem) {
  const langCode = langSelectElem.value;
  if (!langCode || langCode.length <= 0) {
    console.error('No language Selected. Please Select a language.');
    return;
  }

  fetch('https://hellosalut.stefanbohacek.dev/?lang=' + langCode)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Error while fetching hello message');
      }

      return response.json();
    })
    .then((json) => {
      outputElem.innerHTML = json.hello;
    })
    .catch((error) => {
      console.error(error);
    });
}

function onPageLoaded () {
  const outputElem = document.querySelector('#hello');
  const langSelectElem = document.querySelector('#language_code');

  document.querySelector('#btn_translate').addEventListener('click', () => fetchAndDisplayHello(langSelectElem, outputElem));
}

document.addEventListener('DOMContentLoaded', onPageLoaded);
