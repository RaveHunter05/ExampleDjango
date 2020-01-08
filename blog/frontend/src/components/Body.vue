<template>
  <div class="encierro">
    <div class="premiere" >
        
    </div>
    <div class="secondaire">
        <p>"La música es el alimento del alma"</p>
        <p>-Arthur Schopenhauer</p>
        <p>{{message}}</p>
    </div>
    <div class="troisieme">
        <p>
          Nosotros amamos la música, 
          y creamos esta pagina para que 
          vos la disfrutes tanto como nosotros, 
          al final esto es lo que mueve al mundo. ¡Que disfrutes!
          </p>
    </div>

    <div class='quatrieme'>
      <p>Trending</p>
      <div class="musica">
        <section>
        <p  >Destacados</p>
        <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
      </section>
       <section>
        <p  >Destacados</p>
        <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
      </section>
       <section>
        <p  >Destacados</p>
        <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
      </section>
      
      </div>
      <button class="btn">
      Pruébalo ahora
    </button> 
    </div>

    <Beneficios/>
  </div>
</template>

<script>
import Beneficios from './Beneficios.vue';
import Store from '../store/store'


export default {
  name: 'Body',
  components:{
    Beneficios
  },
  data(){
    return{
      items: []
    }
  },
  props: {
  },
  created(){
    fetch('http://127.0.0.1:8000/api/v1.0/cancion/3/')
  .then(response => response.json())
  .then(json => this.items=json)
  },
  methods:{
 
  },
  computed: {
    message () {
      return Store.state.message;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  @import '../css/body.scss';
</style>
