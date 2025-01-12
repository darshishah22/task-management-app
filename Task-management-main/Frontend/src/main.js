import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.css'; 
import 'mdb-vue-ui-kit/css/mdb.min.css';

const app = createApp(App)

app.use(router)

app.mount('#app')
