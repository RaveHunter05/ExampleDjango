<template>
  <div class="principal">
    <div class="login">
    <h2>Login</h2>
    <input type="text" placeholder="Usuario">
    <input type="password" placeholder="contraseña">
    <div class="registrar">
      <a href="">¿Olvidaste tu contraseña?</a>
    </div>
    <div class="redes">
        <i class="fab fa-facebook-f"></i>
        <i class="fab fa-google"></i>
        <i class="fab fa-twitter"></i>
    </div>
    <input type="button" value="Entrar" class="btn" @click="ingresar()">

  </div>
  </div>
</template>

<script>
export default {
name:'Login',
methods:{
  ingresar(){
    this.$router.replace('/body2');
    this.$emit('actualizar',1);
  }
}
}
</script>

<style  lang='scss' scoped>
    @import '../css/login.scss'
</style>