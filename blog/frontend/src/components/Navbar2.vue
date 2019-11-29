<template>
  <div>
      <div class="navbar">
      <h2 @click="principal()">PyShark2</h2>
      <nav class="derechaNavBar">
          
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