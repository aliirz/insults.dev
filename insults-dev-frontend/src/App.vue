<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header class="hero-section">
    <h1>Insults.dev - Unleash Your Code Banter!</h1>
    <p>Tired of the same old programmer jokes? Let ChatGPT write them so that you dont have to.</p>
</header>


  <RouterView />
</template>

<style scoped>


.hero-section {
    background-color: #282c34; /* Dark background for contrast */
    color: #ffffff; /* White text */
    padding: 60px 0; /* Vertical padding */
    text-align: center; /* Centered text */
    font-family: 'Arial', sans-serif; /* Sample font, you can replace with your preferred font */
}

.hero-section h1 {
    font-size: 2.5em; /* Large text for the main header */
    margin-bottom: 20px; /* Spacing between header and description */
}

.hero-section p {
    font-size: 1.2em; /* Slightly larger text for the description */
    max-width: 800px; /* Control the width of the description */
    margin: 0 auto; /* Center the description if it's less than the max width */
}

</style>
