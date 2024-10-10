<template>
    <div class="container mt-5">
      <div class="card mx-auto" style="max-width: 400px;">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Register</h2>
          <form @submit.prevent="registerUser">
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input type="text" v-model="username" class="form-control" id="username" placeholder="Enter your username" />
            </div>
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" id="password" placeholder="Enter your password" />
            </div>
            <button type="submit" class="btn btn-primary w-100">Register</button>
          </form>
          <p v-if="message" class="mt-3 alert alert-warning text-center">{{ message }}</p>
          
          <!-- Link to Login Page -->
          <p class="text-center mt-4">
            Already have an account? <router-link to="/login">Log in here!</router-link>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import api from '@/api';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'Register',
    data() {
      return {
        username: '',
        password: '',
        message: '',
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      async registerUser() {
        try {
          const response = await api.post('/register', {
            username: this.username,
            password: this.password,
          });
          this.message = response.data.message;
          this.router.push('/login'); // Redirect to login after successful registration
        } catch (error: any) {
          this.message = error.response?.data.error || 'An error occurred';
        }
      },
    },
  });
  </script>
  
  <style scoped>
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }
  </style>