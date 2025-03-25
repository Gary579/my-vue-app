import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/Login.vue'
import HomePage from '../views/Home.vue'

const routes = [
  { path: '/', component: LoginPage },
  { path: '/home', component: HomePage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router