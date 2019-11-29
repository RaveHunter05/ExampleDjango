<template>
  <div id="app" class="page-container" @actualizar="alert('puto el que lea')">

    <Navbar v-if="tipoDeNav==0" @clicked='onClickChild($event)'/>
    <Navbar2 v-if="tipoDeNav==1" @clicked2='onClickChild($event)'/>
    <router-view> </router-view>
    <Footer/>
  </div>
</template>

<script>


import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import Navbar2 from './components/Navbar2.vue';

export default {
  name: 'app',
  data(){
    return{
      tipoDeNav:''
    }
  },
  components: {
    Navbar,
    Footer,
    Navbar2
  },
  methods:{
    onClickChild (value) {
      this.tipoDeNav=value;
    }
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
