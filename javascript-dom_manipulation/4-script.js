// Cache .my_list element to avoid query on everry click
const myList = document.querySelector('.my_list');

// Add new item to .my_list when #add_item is clicked
document.querySelector('#add_item').addEventListener('click', () => {
  const item = document.createElement('li');
  item.innerHTML = 'Item';
  myList.append(item);
});
