import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';

const routes = [
  {
    path: '/',
    redirect: '/login', // Redirect root to login page by default
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard to prevent unauthorized access to protected routes
router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
    next('/login'); // Redirect to login if trying to access a protected route without being logged in
  } else if (to.path === '/login' && isLoggedIn) {
    next('/notes'); // If logged in, redirect from login page to notes page
  } else {
    next(); // Otherwise, allow navigation
  }
});

export default router;
