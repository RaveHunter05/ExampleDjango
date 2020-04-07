<template>
  <div class="totalidad">
    <div class="body">
      <div class="buscador" v-if="playVisibility==true">
        <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
        <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt />
        <h3 class="cancion pointer" @click="album">Stressed out</h3>
        <h3 class="artista pointer" @click="artista">Twenty One Pilots</h3>
        <label class="album1 pointer" @click="album">Blurryface</label>
        <div class="iconos">
          <i class="fas fa-ellipsis-h noplay"></i>
          <i class="fas fa-step-backward noplay"></i>
          <i class="fas fa-play play"></i>
          <i class="fas fa-step-forward noplay"></i>
          <i class="far fa-heart noplay"></i>
        </div>
      </div>
      <input class="busqueda" type="text" placeholder="Realice su búsqueda" />
      <section class="section">
        <h2>Destacados</h2>
        <div class="destacados">
          <div @click="cambiarPlay" class="album">
            <img
              class="imagen"
              src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg"
              alt
            />
            <label for>Twenty One Pilots</label>
          </div>

          <div class="album" v-for="artista in artistas" :key="artista.id">
            <img class="imagen" :src="artista.foto" alt />
            <label class="titulo" for>{{artista.nombre_artistico}}</label>
          </div>
        </div>
      </section>
      <section class="section">
        <h2>Albumes</h2>
        <!-- corregir esto que no da -->
        <div class="destacados">
          <div class="album" v-for="album in albumes" :key="album.id" @click="irAlbum(album)">
            <img class="imagen" :src="album.caratula" alt />
            <label class="titulo" for>{{album.titulo}}</label>
          </div>
        </div>
      </section>
      <section class="section">
        <h2>Temas</h2>
        <div class="destacados">
          <div class="album" v-for="destacado in destacados" :key="destacado.id" @click="enviarCancion(destacado.sonido)">
            <img class="imagen" :src="destacado.caratula" alt />
            <label class="titulo" for>{{destacado.titulo}}</label>
          </div>
        </div>
      </section>
      <section class="section">
        <h2>Artistas</h2>
        <div class="destacados artistas">
          <div class="album" v-for="artista in artistas" :key="artista.id">
            <img class="imagen" :src="artista.foto" alt />
            <label class="titulo" for>{{artista.nombre_artistico}}</label>
          </div>
        </div>
      </section>
      <section class="section">
        <h2>Playlists</h2>
        <div class="destacados">
          <div class="album" v-for="playlist in playlists" :key="playlist.id" @click="irPlaylist(playlist)">
            <img class="imagen" :src="playlist.caratula" alt />
            <label class="titulo" for>{{playlist.titulo}}</label>
          </div>
        </div>
      </section>
      
      <!-- <section class="section">
                <h2>Podcasts</h2>
                <div class="destacados">
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>

                </div>
      </section>-->
    </div>
    <Play :cancion="this.pasarCancion"/>
  </div>
</template>

<script>

import Play from './Play';

export default {
  name: "Body2",
  data() {
    return {
      playVisibility: false,
      destacados: [],
      temas: [],
      artistas: [],
      playlists: [],
      albumes:[],
      pasarCancion:''
    };
  },
  components:{
      Play
  },
  methods: {
    cambiarPlay() {
      this.playVisibility = !this.playVisibility;
    },
    artista() {
      this.$router.replace("/artista");
    },
    irAlbum(variableAlbum) {
      this.$router.replace(
        {name:'album', 
        params:{
        imagen:variableAlbum.caratula,
        titulo:variableAlbum.titulo,
        idAlbum:variableAlbum.id
        }});
    },
    irPlaylist(variablePlaylist){
      this.$router.replace({name:'playlist',params:{
        titulo:variablePlaylist.titulo,
        imagen:variablePlaylist.caratula,
        artista:variablePlaylist.usuario,
        idPlaylist:variablePlaylist.id
      }})
    },
    enviarCancion(valor){
        this.pasarCancion=valor
        // alert(valor)
        // alert(this.pasarCancion)
    }
  },
  created() {
    
    fetch("http://127.0.0.1:8000/api/v1.0/cancion/")
      .then(response => response.json())
      .then(json => (this.destacados = json));

    fetch('http://127.0.0.1:8000/api/v1.0/cantante/')
        .then(response=>response.json())
        .then(json=>(this.artistas=json))

    fetch('http://127.0.0.1:8000/api/v1.0/playlist/')
        .then(response=>response.json())
        .then(json=>(this.playlists=json))

    fetch("http://127.0.0.1:8000/api/v1.0/album/")
      .then(response => response.json())
      .then(json => (this.albumes = json));
  }
};
</script>

<style lang="scss" scoped>
@import "../css/body2.scss";
</style>