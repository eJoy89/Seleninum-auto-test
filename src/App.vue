<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input v-model="inputText" placeholder="Enter something" />
    <button @click="displayMessage">Display Message</button>
    <p v-if="showMessage">{{ inputText }}</p>
  
  <BoxTest 
    :changeColour="changeColour"
  />

  <div class="box" :style="{background: changeColour ? 'blue' : 'pink'}"></div>

  <button id="color-change-button" @click="colorChange">색변경</button>
  </div>
</template>

<script>
import BoxTest from './components/BoxTest.vue';


export default {
  components: {
    BoxTest
  },
  data() {
    return {
      message: "Hello Vue!",
      inputText: "",
      showMessage: false,
      changeColour: true,
    };
  },
  methods: {
    displayMessage() {
      this.showMessage = true;
    },
    colorChange() {
      this.changeColour = !this.changeColour;
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
.box{
  width: 300px;
  height: 300px;
}
</style>
