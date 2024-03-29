const myList = document.querySelector('.my_list');

document.querySelector('#add_item').addEventListener('click', function (e) {
  const item = document.createElement('li');
  item.innerHTML = 'Item';
  myList.append(item);
});
