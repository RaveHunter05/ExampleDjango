<template>
  <div>
    <div class="navbar">
      <h2 @click="principal()">PyShark2</h2>
      <nav class="derechaNavBar">
        <div>
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/a/a9/Corvus_corone_-near_Canford_Cliffs%2C_Poole%2C_England-8.jpg"
            alt
          />
        </div>
        <div class="perfil" @click="changeVisibility">
          <label class="nombre">RaveHunter05</label>
          <label>paulsotelo97@gmail.com</label>
        </div>
      </nav>
    </div>
    <div v-if="escondido==true" class="emergente">
        <div class="items" @click="irUsuario">
            <i class="fas fa-user-circle"></i>
            <label>Perfil</label>    
        </div>
        <div class="items">
            <i class="fas fa-fire-alt"></i>
            <label>Cambiar plan</label>
        </div>
        <div class="items">
            <i class="fas fa-cog"></i>
            <label>Congifuración</label>
        </div>
        <div class="items">
            <i class="fas fa-question-circle"></i>
            <label>Ayuda</label>
        </div>
        <div @click="irPrincipal" class="items">
            <i class="far fa-times-circle"></i>
            <label>Cerrar</label>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  components: {},
  data() {
    return {
        escondido:false
    };
  },
  methods: {
    principal() {
      this.$router.replace("/body2");
      this.$emit("clicked2", 0);
    },
    changeVisibility(){
        this.escondido=!this.escondido;
    },
    irUsuario(){
        this.$router.replace('/usuario');
        this.escondido=false;
    },
    irPrincipal(){
        this.$router.replace('/');
        this.$emit("clicked2", 0);
    }
  }
};
</script>
    
<style lang='scss' scoped>
@import "../css/navbar2.scss";
</style>