<template>
  <div class="body">
    <div class="principal2">
      <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
      <img
        src="https://los40es00.epimg.net/los40/imagenes/2019/03/01/musica/1551442540_929381_1551445076_noticia_normal.jpg"
        alt
      />
      <h3>Twenty One Pilots</h3>
      <label>44,099,999 oyentes mensuales</label>
    </div>

    <div class="albumesArtistas">
      <h3>Albumes</h3>
      <section class="albumes">
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="https://m.media-amazon.com/images/I/716qi-1n5GL._SS500_.jpg" alt />
          <label>Twenty One Pilots</label>
        </div>
        <div class="albumIndividual">
          <img src="http://pm1.narvii.com/6607/66807819d06fb9df65828d12619e897fd3f6b74f_00.jpg" alt />
          <label>Regional At Best</label>
        </div>
        <div class="albumIndividual">
          <img src="https://img.cdandlp.com/2018/11/imgL/119362521.jpg" alt />
          <label>Vessel</label>
        </div>
        <div class="albumIndividual">
          <img src="https://themusickblog.files.wordpress.com/2016/08/blurryface.jpg?w=1400" alt />
          <label>Blurryface</label>
        </div>
        <div class="albumIndividual">
          <img
            src="https://canchageneral.com/wp-content/uploads/2019/02/81znz4j2UTL._SL1425_.jpg"
            alt
          />
          <label>Trench</label>
        </div>
      </section>
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
          <td><i class="far fa-heart pointer"></i></td>
          <td><i class="fas fa-ellipsis-h pointer"></i></td>
        </tr>
        <tr>
          <td>2</td>
          <td>Stressed Out</td>
          <td>X</td>
          <td><i class="far fa-heart pointer"></i></td>
          <td><i class="fas fa-ellipsis-h pointer"></i></td>
        </tr>
        <tr>
          <td>3</td>
          <td>Ride</td>
          <td>X</td>
          <td><i class="far fa-heart pointer"></i></td>
          <td><i class="fas fa-ellipsis-h pointer"></i></td>
        </tr>
        <tr>
          <td>4</td>
          <td>Fairly Local</td>
          <td>X</td>
          <td><i class="far fa-heart pointer"></i></td>
          <td><i class="fas fa-ellipsis-h pointer"></i></td>
        </tr>
        <tr>
          <td>5</td>
          <td>Tear In My Heart</td>
          <td>X</td>
          <td><i class="far fa-heart pointer"></i></td>
          <td><i class="fas fa-ellipsis-h pointer"></i></td>
        </tr>
        </tbody>
      </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'Artista',
  methods:{
    cambiarPlay(){
      this.$router.replace('/body2');
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../css/Artista.scss";
</style>