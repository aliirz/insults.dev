<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'InsultGenerator',
  data() {
    return {
      languages: [
        "JavaScript", "Python", "Java", "C#", "TypeScript", "PHP", "C++", "C", 
        "Ruby", "Swift", "Node.js", "React.js", "Angular", ".NET Core", 
        "Spring Boot", "Django", "Flask", "Vue.js", "Express", "Laravel"
      ],
      language: "",
      insult: "",
      isLoading: false
    }
  },
  methods: {
    generateInsult(_language: string) {
      this.isLoading = true;
      fetch(`http://localhost:8000/${_language}`)
        .then(response => response.json())
        .then(data => {
          this.insult = data.insult;
          this.isLoading = false;
        })
        .catch(error => {
          console.error(error);
          this.isLoading = false;
        });
    }
  }
});
</script>

<template>
  <div class="container">
    <select v-model="language" :disabled="isLoading">
      <option v-for="lang in languages" :key="lang" :value="lang">{{ lang }}</option>
    </select>
    <button @click="generateInsult(language)" :disabled="isLoading">
      <span v-if="isLoading">Loading...</span>
      <span v-else>Generate</span>
    </button>
    <div v-if="insult">
      <p>{{ insult }}</p>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* height: 100vh; */
}

select, button {
  margin: 10px;
  padding: 10px;
  font-size: 16px;
}

p {
  text-align: center;
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 20px;
  user-select: all; /* Makes it easier to select the text for copying */
}
</style>
