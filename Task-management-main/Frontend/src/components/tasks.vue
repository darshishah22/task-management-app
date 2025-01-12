<template>
  <section class="vh-100 gradient-custom-2">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-md-12 col-xl-10">
          <div class="card mask-custom">
            <div class="card-body p-4 text-white">
              <div class="text-center pt-3 pb-2">
                <!-- Task Manager Header -->
                <img
                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-todo-list/check1.webp"
                  alt="Check"
                  width="60"
                />
                <h2 class="my-4">Task Manager</h2>
              </div>

              <!-- Task Form Inputs -->
              <div class="input-group mb-3">
                <!-- Task Title -->
                <div class="form-group me-3">
                  <label for="task-title">Task Title</label>
                  <input
                    id="task-title"
                    type="text"
                    class="form-control"
                    placeholder="Task Title"
                    v-model="TaskText"
                    required
                  />
                </div>
                <!-- Task Description -->
                <div class="form-group me-3">
                  <label for="task-description">Description</label>
                  <input
                    id="task-description"
                    type="text"
                    class="form-control"
                    placeholder="Task Description"
                    v-model="TaskDescription"
                    required
                  />
                </div>
                <!-- Task Priority -->
                <div class="form-group me-3">
                  <label for="task-priority">Priority</label>
                  <select
                    id="task-priority"
                    class="form-select"
                    v-model="TaskPriority"
                    required
                  >
                    <option value="Low">Low</option>
                    <option value="Medium">Medium</option>
                    <option value="High">High</option>
                  </select>
                </div>
                <!-- Task Status -->
                <div class="form-group me-3">
                  <label for="task-status">Status</label>
                  <select
                    id="task-status"
                    class="form-select"
                    v-model="TaskStatus"
                  >
                    <option value="To Do">To Do</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Done">Done</option>
                  </select>
                </div>
                <!-- Task Date -->
                <div class="form-group me-3">
                  <label for="task-date">Due Date</label>
                  <input
                    id="task-date"
                    type="date"
                    class="form-control"
                    v-model="TaskDate"
                    :min="new Date().toISOString().split('T')[0]"
                    required
                    onkeydown="return false"
                  />
                </div>
                <!-- Submit Button -->
                <div class="form-group">
                  <label>&nbsp;</label>
                  <button class="btn btn-success w-100" type="button" @click="AddTask">
                    {{ editedTask ? "Edit Task" : "Add Task" }}
                  </button>
                </div>
              </div>

              <!-- Task List Table -->
              <table class="table text-white mb-0">
                <thead>
                  <tr class="table-header">
                    <th scope="col">Task</th>
                    <th scope="col">Description</th>
                    <th scope="col">Priority</th>
                    <th scope="col">Status</th>
                    <th scope="col">Date</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="task in apidata"
                    :key="task.id"
                    class="fw-normal"
                  >
                    <!-- Display Task Information -->
                    <td class="align-middle">
                      <span
                        :class="{'text-decoration-line-through': task.status === 'Done'}"
                      >
                        {{ task.task }}
                      </span>
                    </td>
                    <td class="align-middle">{{ task.description }}</td>
                    <td class="align-middle">{{ task.priority }}</td>
                    <td class="align-middle">
                      <!-- Task Status Badge -->
                      <span
                        :class="{
                          'badge bg-danger': task.status === 'To Do',
                          'badge bg-warning': task.status === 'In Progress',
                          'badge bg-success': task.status === 'Done',
                        }"
                        @click="changestatus(task.id)"
                      >
                        {{ task.status }}
                      </span>
                    </td>
                    <td class="align-middle">{{ task.date }}</td>
                    <td class="align-middle">
                      <!-- Task Action Icons -->
                      <a href="#" title="Done" @click="done(task.id)">
                        <i class="fas fa-check-circle me-3" style="color: #256B03;"></i>
                      </a>
                      <a href="#" title="Edit" @click="edit(task.id)">
                        <i class="fas fa-pen-alt fa-lg text-dark me-3"></i>
                      </a>
                      <a href="#" title="Remove" @click="deleteTask(task.id)">
                        <i class="fas fa-trash-alt fa-lg text-warning"></i>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  name: "tasks-components-page",
  data() {
    return {
      TaskText: "",
      TaskDescription: "",
      TaskPriority: "Low",
      TaskStatus: "To Do", // Default to "To Do"
      TaskDate: "",
      apidata: [],
      editedTask: null,
    };
  },
  methods: {
    // Fetch list of tasks from API
    async listapitasks() {
      try {
        const response = await axios.get("http://127.0.0.1:8000");
        this.apidata = response.data;
      } catch (error) {
        console.error("Error fetching tasks:", error);
      }
    },
    // Add or Edit task
    async AddTask() {
      if (!this.TaskText || !this.TaskDescription || !this.TaskPriority || !this.TaskDate) {
        alert("Please fill all the fields");
        return;
      }
      const taskData = {
        task: this.TaskText,
        description: this.TaskDescription,
        priority: this.TaskPriority,
        status: this.TaskStatus,
        date: this.TaskDate,
      };
      try {
        if (this.editedTask === null) {
          await axios.post("http://127.0.0.1:8000/create/", taskData);
        } else {
          await axios.put(
            `http://127.0.0.1:8000/editTask/${this.editedTask}`,
            taskData
          );
        }
        this.listapitasks();
        this.resetForm();
      } catch (error) {
        console.error("Error adding/updating task:", error);
      }
    },
    // Reset form after add/edit
    resetForm() {
      this.TaskText = "";
      this.TaskDescription = "";
      this.TaskPriority = "Low";
      this.TaskStatus = "To Do"; // Reset to default
      this.TaskDate = "";
      this.editedTask = null;
    },
    // Change task status
    async changestatus(id) {
      const task = this.apidata.find((task) => task.id === id);
      if (task) {
        const availableStatus = ["To Do", "In Progress", "Done"];
        const currentIndex = availableStatus.indexOf(task.status);
        const newIndex = (currentIndex + 1) % availableStatus.length;
        try {
          await axios.patch(`http://127.0.0.1:8000/editTask/${id}`, {
            status: availableStatus[newIndex],
          });
          this.listapitasks();
        } catch (error) {
          console.error("Error changing status:", error);
        }
      }
    },
    // Mark task as done
    async done(id) {
      try {
        await axios.patch(`http://127.0.0.1:8000/editTask/${id}`, {
          status: "Done",
        });
        this.listapitasks();
      } catch (error) {
        console.error("Error marking task as done:", error);
      }
    },
    // Delete a task
    async deleteTask(id) {
      try {
        if (this.editedTask === id) {
          // Reset form if task being deleted is the one being edited
          this.resetForm();
        }
        await axios.delete(`http://127.0.0.1:8000/editTask/${id}`);
        this.listapitasks();
      } catch (error) {
        console.error("Error deleting task:", error);
      }
    },
    // Edit an existing task
    edit(id) {
      const task = this.apidata.find((task) => task.id === id);
      if (task) {
        this.TaskText = task.task;
        this.TaskDescription = task.description;
        this.TaskPriority = task.priority;
        this.TaskStatus = task.status;
        this.TaskDate = task.date;
        this.editedTask = id;
      }
    },
  },
  mounted() {
    this.listapitasks();
  },
};
</script>

<style scoped>
.vh-100 {
  height: 100vh;
}

.gradient-custom-2 {
  background: #944ae3;
  background: linear-gradient(to right, #8522e9, #7571ed);
}

.mask-custom {
  background-color: rgba(205, 175, 215, 0.7);
}

.table-header {
  background-color: #6c757d;
}

.table-header th {
  color: white;
}

.badge {
  cursor: pointer;
}

table {
  table-layout: fixed; 
  word-wrap: break-word; 
}

.table td, .table th {
  white-space: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
  vertical-align: top; 
}


.table td:nth-child(2) {
  max-width: 300px; 
}
</style>
