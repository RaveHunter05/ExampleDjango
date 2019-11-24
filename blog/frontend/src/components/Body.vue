<template>
  <div class="encierro">
    <div class="premiere" >
        
    </div>
    <div class="secondaire">
        <p>"La música es el alimento del alma"</p>
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
import Beneficios from './Beneficios.vue'
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
    fetch('https://jsonplaceholder.typicode.com/posts/1/comments')
  .then(response => response.json())
  .then(json => this.items=json)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  @import '../css/body.scss';
</style>
