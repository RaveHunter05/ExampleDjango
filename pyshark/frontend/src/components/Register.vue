<template>
  <div class="principal">
      <div class="login">
        <h2>Sign up</h2>
        <input type="text" placeholder="Usuario">
        <input type="text" placeholder="E-mail">
        <input type="text" placeholder="Repetir correo">
        <input type="password" placeholder="Contraseña">
        <input type="password" placeholder="Repetir contraseña">
        <div class="redes">
          <i class="fab fa-facebook-f"></i>
          <i class="fab fa-google"></i>
          <i class="fab fa-twitter"></i>
        </div>
        <button class="btn" >Regístrate</button>
      </div>

  </div>
</template>

<script>
export default {
  name:'Register'
}
</script>

<style lang='scss' scoped>
    @import '../css/register.scss'
</style>