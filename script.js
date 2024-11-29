document.getElementById('taskForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const taskData = {
        title: document.getElementById('title').value,
        description: document.getElementById('description').value,
        due_date: document.getElementById('due_date').value,
    };

    const response = await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(taskData)
    });

    const result = await response.json();
    console.log(result);
    loadTasks();
});

// Load tasks when the page is loaded
window.onload = loadTasks;

async function loadTasks() {
    const response = await fetch('/tasks');
    const tasks = await response.json();
    
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
    
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = `${task.title} - ${task.status}`;
        taskList.appendChild(li);
    });
}
