#!/usr/bin/node

const request = require('request');

/**
 * countTasks - count completed tasks by user
 * @dict: dictionary of users
 * @task: task to count
 *
 * Return: dictionary of user and their nuumber of completed tasks
 */
function countTasks (dict, task) {
  if (task.completed === false) return dict;

  const user = task.userId.toString();

  dict[user] = (dict[user] || 0) + 1;

  return dict;
}

request(process.argv[2], (err, _, body) => {
  if (err) throw err;

  const json = JSON.parse(body);
  const userDict = json.reduce(countTasks, {});

  console.log(userDict);
});
