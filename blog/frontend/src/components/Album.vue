<template>
  <div class="body">
      <div class="principal1">
         <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
            <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
            <h3>Blurryface</h3>
            <label>Twenty One Pilots</label>
        <div class="iconos">
          <i class="fas fa-ellipsis-h pointer"></i>
          <button class="btn pointer">
            Reproducir aleatoriamente
          </button>
          <i class="far fa-heart pointer"></i>
        </div>
      </div>
      <div class="tableArtistas">
      <div class="tbl-header">
        <table cellpadding="0" cellspacing="0" border="0">
          <thead>
            <tr>
              <th>#</th>
              <th>Nombre</th>
              <th>Duracion</th>
              <th>Favoritas</th>
              <th>Opciones</th>
            </tr>
          </thead>
        </table>
      </div>
      <div class='tbl=content'>
      <table cellpadding="0" cellspacing="0" border="0">
        <tbody>
        <tr>
          <td>1</td>
          <td>Heavydirtysoul</td>
          <td>X</td>
          <td><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        <tr>
          <td>2</td>
          <td>Stressed Out</td>
          <td>X</td>
          <td><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        <tr>
          <td>3</td>
          <td>Ride</td>
          <td>X</td>
          <td><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        <tr>
          <td>4</td>
          <td>Fairly Local</td>
          <td>X</td>
          <td><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        <tr>
          <td>5</td>
          <td>Tear In My Heart</td>
          <td>X</td>
          <td><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        </tbody>
      </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'Album',
  methods:{
    cambiarPlay(){
      this.$router.replace('/body2');
    }
  }

}
</script>

<style lang="scss" scoped>
  @import '../css/Album.scss'
</style>