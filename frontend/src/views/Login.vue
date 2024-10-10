<template>
    <div class="container mt-5">
      <div class="card mx-auto" style="max-width: 400px;">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Login</h2>
          <form @submit.prevent="loginUser">
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input type="text" v-model="username" class="form-control" id="username" placeholder="Enter your username" />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" id="password" placeholder="Enter your password" />
            </div>
            <button type="submit" class="btn btn-primary w-100">Login</button>
          </form>
          <p v-if="message" class="mt-3 alert alert-warning text-center">{{ message }}</p>
  
          <!-- Link to Register Page -->
          <p class="text-center mt-4">
            Not registered yet? <router-link to="/register">Register here!</router-link>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useAuth } from '@/auth';
  import api from '@/api';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'Login',
    setup() {
      const router = useRouter();
      const { login } = useAuth();
  
      // Define reactive state variables
      const username = ref<string>('');
      const password = ref<string>('');
      const message = ref<string>('');
  
      // Login function
      const loginUser = async () => {
        try {
          const response = await api.post('/login', {
            username: username.value,
            password: password.value,
          });
          login(response.data.token); // Use the global login function to set the token
          router.push('/notes'); // Redirect to Notes page after successful login
        } catch (error: any) {
          message.value = error.response?.data.error || 'Invalid username or password';
        }
      };
  
      return {
        username,
        password,
        message,
        loginUser,
      };
    },
  });
  </script>
  
  <style scoped>
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }
  </style>
  