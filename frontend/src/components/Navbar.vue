<template>
    <div>
      <!-- Navigation Bar -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <!-- Logo -->
          <router-link class="navbar-brand d-flex align-items-center" to="/">
            The Selection Lab Notepad++
          </router-link>
  
          <button 
            class="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <!-- Show these links when the user is logged out -->
              <li class="nav-item" v-if="!isLoggedIn">
                <router-link class="nav-link" to="/login">Login</router-link>
              </li>
              <li class="nav-item" v-if="!isLoggedIn">
                <router-link class="nav-link" to="/register">Register</router-link>
              </li>
              
              <!-- Show these links when the user is logged in -->
              <li class="nav-item" v-if="isLoggedIn">
                <router-link class="nav-link" to="/notes">My Notes</router-link>
              </li>
              <li class="nav-item" v-if="isLoggedIn">
                <button class="btn btn-link nav-link" @click="logout">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
      <!-- Router View -->
      <router-view></router-view>
    </div>
  </template>
  
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default defineComponent({
    name: 'App',
    setup() {
      const router = useRouter();
      const isLoggedIn = ref(!!localStorage.getItem('token')); // Use ref for reactivity
  
      // Logout function
      const logout = () => {
        localStorage.removeItem('token'); // Remove the token to log out the user
        isLoggedIn.value = false; // Update the login state
        router.push('/login'); // Redirect to login page after logout
      };
  
      return {
        isLoggedIn,
        logout,
      };
    },
  });
  </script>
  
  <style scoped>
  .navbar {
    margin-bottom: 20px;
  }
  
  .nav-link {
    cursor: pointer;
  }
</style>