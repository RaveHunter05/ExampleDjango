<template>
  <div>
      <div class="navbar">
    <div class="izquierdaNavBar">
        <h2><router-link class='h2' to='/'>PyShark</router-link></h2>
    </div>
      <nav class="derechaNavBar">
          <ul >
              <li>Escuchar</li>
              <li>Ayuda</li>
              <li>|</li>
              <li @click="logearse">Iniciar Sesión</li>
              <li @click='registro'>Registrarse</li>
          </ul>
      </nav>
  </div>
  <div v-if="login==true">
      <Login />
  </div>

  <div v-if="register==true">
      <Register/>
  </div>
  </div>
</template>

<script>
import Login from './Login';
import Register from './Register'

export default {
    name:'Footer',
    components:{
        Login,
        Register
    },
    data(){
        return{
            login:false,
            register:false
        }
    },
    methods:{
        logearse(){
            if(this.register==true){
                this.register=!this.register;
            }
            this.login=!this.login;
        },
        registro(){
            if(this.login==true){
                this.login=!this.login;
            }
            this.register=!this.register;
        },
        // cambioNav(value){
        //     this.$emit('clicked',value)
        // }
    }
}
</script>
    
<style lang='scss' scoped>
   @import '../css/navbar.scss'
</style>