<template>
  <div class="container text-center">
    <tasks :data="data" />
  </div>
</template>

<script>
import tasks from '@/components/tasks.vue'

export default {
  name: 'Tasks View page',
  components: {
    tasks,
  },
}
</script>

<style scoped>
/* Scoped style for the component */
.container {
  padding: 20px;
  background: linear-gradient(to right, #8522e9, #7571ed);
}
</style>
