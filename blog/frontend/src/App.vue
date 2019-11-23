<template>
  <div id="app" class="page-container">
    <Navbar/>
    <Body/>
    <Footer/>
  </div>
</template>

<script>
import Body from './components/Body.vue';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue'

export default {
  name: 'app',
  components: {
    Body,
    Navbar,
    Footer

  }
}
</script>

<style>
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; */
}

html, body{
   min-height: 100%;
    width: 100%;
}

.page-container {
  position: relative;
    height: 100vh;
}
</style>
