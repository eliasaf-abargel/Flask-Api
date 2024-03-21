# Get all tasks
curl http://127.0.0.1:5000/tasks

# Get a specific task by ID
curl http://127.0.0.1:5000/tasks/1

# Create a new task
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Task","details":"Task details"}' http://127.0.0.1:5000/tasks

# Update a task
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Task","details":"Updated details"}' http://127.0.0.1:5000/tasks/1

# Delete a task
curl -X DELETE http://127.0.0.1:5000/tasks/1