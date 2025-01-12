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
