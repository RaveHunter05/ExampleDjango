<template>
  <div>
      <div class="navbar">
      <h2 @click="principal()">PyShark2</h2>
      <nav class="derechaNavBar">
          <div>
              <img src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Corvus_corone_-near_Canford_Cliffs%2C_Poole%2C_England-8.jpg" alt="">
          </div>
          <div class="perfil">
              <label class="nombre">RaveHunter05</label>
              <label>paulsotelo97@gmail.com</label>
          </div>
      </nav>
  </div>
  </div>
</template>

<script>


export default {
    name:'Footer',
    components:{

    },
    data(){
        return{

        }
    },
    methods:{
        principal(){
            this.$router.replace('/');
            this.$emit('clicked2', 0)
        }
    }
}
</script>
    
<style lang='scss' scoped>
   @import '../css/navbar2.scss'
</style>