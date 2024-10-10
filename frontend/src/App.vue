<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <!-- Logo and App Name -->
        <router-link class="navbar-brand d-flex align-items-center" to="/">
          The Selecion Lab Notepad++
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
import { defineComponent } from 'vue';
import { useAuth } from '@/auth';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'App',
  setup() {
    const { isLoggedIn, logout } = useAuth();
    const router = useRouter();

    const handleLogout = () => {
      logout();
      router.push('/login'); // Redirect to login page after logout
    };

    return {
      isLoggedIn,
      logout: handleLogout,
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
