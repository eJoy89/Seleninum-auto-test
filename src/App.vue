<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input v-model="inputText" placeholder="Enter something" />
    <button @click="displayMessage">Display Message</button>
    <p v-if="showMessage">{{ inputText }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Hello Vue!",
      inputText: "",
      showMessage: false
    };
  },
  methods: {
    displayMessage() {
      this.showMessage = true;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
