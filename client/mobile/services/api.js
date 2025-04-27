import axios from 'axios';

const API = axios.create({
  baseURL: 'http://10.0.0.82:8000', // your backend URL
  timeout: 5000,
});

// Function to fetch workouts
export const fetchWorkouts = async () => {
    // try {
      const response = await API.get('/workouts');
      return response.data;
    // } catch (error) {
    //   if (error.response) {
    //     // Server responded with a status other than 2xx
    //     console.error('Response error:', error.response.data);
    //     console.error('Response status:', error.response.status);
    //   } else if (error.request) {
    //     // Request was made but no response received
    //     console.error('Request error:', error.request);
    //   } else {
    //     // Something happened setting up the request
    //     console.error('Error:', error.message);
    //   }
    //   throw error;  // Rethrow the error so you can handle it at a higher level
    // }
  };
  