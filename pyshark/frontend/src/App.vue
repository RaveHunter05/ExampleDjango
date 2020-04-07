<template>
  <div id="app" class="page-container">
    <div v-if="this.$route.path=='/'">
      <Navbar v-if="tipoDeNav==0" />
    </div>
    <div v-else-if="this.$route.path!='/'">
      <Navbar2 />
    </div>
    <router-view> </router-view>
    <Footer/>
    <!-- <Play v-if="this.$route.path=='/body2'"/> -->
  </div>
</template>

<script>


import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';
import Navbar2 from './components/Navbar2.vue';
// import Play from './components/Play.vue';

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
    Navbar2,
    // Play
  },
  methods:{
    onClickChild (value) {
      this.tipoDeNav=value;
    }
  }
}
</script>

<style>

html, body{
   min-height: 100%;
    width: 100%;
}

.page-container {
  position: relative;
    height: 100vh;
}
</style>
