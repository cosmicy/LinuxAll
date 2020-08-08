import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
//import BackTopOne from "../views/BackTopOne";

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
    {
      path: '/BackTopOne',
      name: 'backTopOne',
      component: () => import('../views/BackTopOne')
    },
    {
      path: '/BackTopTwo',
      name: 'backTopTwo',
      component: () => import('../views/BackTopTwo')
    },
    {
      path: '/Login',
      name: 'login',
      component: () => import('../views/Login')
    }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
