import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import Notes from '@/views/Notes.vue';
import EditNote from '@/views/EditNote.vue';

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
  {
    path: '/notes',
    name: 'Notes',
    component: Notes,
    meta: { requiresAuth: true }, // Mark as a protected route
  },
  {
    path: '/notes/edit/:noteId',
    name: 'EditNote',
    component: EditNote,
    meta: { requiresAuth: true }, // Mark as a protected route
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation guard to prevent unauthorized access to protected routes
router.beforeEach((to, from, next) => {
  const isLoggedIn = !!localStorage.getItem('token'); // Checks if there's a token stored (user is logged in)

  // Redirect user to login if they try to access a protected route without being logged in
  if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
    next('/login');
  } else if ((to.path === '/login' || to.path === '/register') && isLoggedIn) {
    next('/notes'); // Redirect logged-in users away from login or register page
  } else {
    next(); // Otherwise, allow the navigation
  }
});

export default router;



