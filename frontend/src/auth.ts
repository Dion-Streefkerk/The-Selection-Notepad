import { ref } from 'vue';

// Global state to manage authentication status
const isLoggedIn = ref(!!localStorage.getItem('token'));

export function useAuth() {
  const login = (token: any) => {
    localStorage.setItem('token', token);
    isLoggedIn.value = true;
  };

  const logout = () => {
    localStorage.removeItem('token');
    isLoggedIn.value = false;
  };

  return {
    isLoggedIn,
    login,
    logout,
  };
}