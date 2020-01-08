<template>
  <div class="body">
      <div class="principal1">
         <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
            <img :src="this.imagen" alt="">
            <h3>{{titulo}}</h3>
            <label>{{this.nombreUsuario}}</label>
        <div class="iconos">
          <i class="fas fa-ellipsis-h pointer"></i>
          <button class="btn pointer">
            Reproducir aleatoriamente
          </button>
          <i class="far fa-heart pointer"></i>
        </div>
        <label v-show="this.condicional==true">
          {{this.registroCancion}}
        </label>
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
        <tr v-for="cancion in canciones" :key="cancion.id">
          <td>{{cancion.id}}</td>
          <td @click="enviarCancion(cancion.sonido)">{{cancion.titulo}}</td>
          <td>{{cancion.duracion}}</td>
          <td v-if="cancion.corazon==true"><i class="fas fa-heart pointer1"></i></td>
          <td v-if="cancion.corazon==false"><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        </tbody>
      </table>
    <Play :cancion="this.pasarCancion"/>

      </div>
    </div>
  </div>
</template>

<script>

import Play from './Play';

export default {
  name:'Album',
  data(){
    return{
      usuarioAlbum:[],
      contador:[],
      artistaNombre:'',
      cancionAlbum:[],
      contadorCancion:[],
      canciones:[],
      condicional:false,
      pasarCancion:''
    }
  },
  methods:{
    cambiarPlay(){
      this.$router.replace('/body2');
    },
    verNombreUsuario(){
      this.contador=this.usuarioAlbum.filter(d=>d.id==this.artista);
      this.artistaNombre=this.contador[0]["nickname"]

    },
    devolverCanciones(){
      this.contadorCancion=this.cancionAlbum.filter(d=>d.playlist.id==this.idPlaylist)
      for(const i in this.contadorCancion){
        this.canciones.push(this.contadorCancion[i]["cancion_album"]["cancion"])
      }
    },
    playlistUsuario(){
       const t=this;
        fetch("http://127.0.0.1:8000/api/v1.0/usuario/")
          .then(response => response.json())
          .then((res)=>{
            t.usuarioAlbum=JSON.parse(JSON.stringify(res));
            return t.usuarioAlbum
      })
    },
    enviarCancion(dato){
      this.pasarCancion=dato;
    },
    playlistCancion(){
      const t=this;
        fetch("http://127.0.0.1:8000/api/v1.0/playlist_cancion_mixin/")
          .then(response => response.json())
          .then((res)=>{
            t.cancionAlbum=JSON.parse(JSON.stringify(res));
            return t.cancionAlbum
      })
    }
  },
  components:{
    Play
  },
  props:[
    'imagen',
    'titulo',
    'artista',
    'idPlaylist'
  ],
  created(){
    this.playlistUsuario();
    this.playlistCancion();
  },
  computed:{
    nombreUsuario(){
      if(this.usuarioAlbum!=''){
        this.verNombreUsuario();
        return this.artistaNombre;
      }else{
        return 'esta playlist no tiene usuario creador, brutal.jpg';
      }
    },
    registroCancion(){
      if(this.cancionAlbum!=''){
        this.devolverCanciones();
        return  this.canciones
      }
      else{
        return 'este album no contiene canciones'
      }
    }
  }

}
</script>

<style lang="scss" scoped>
  @import '../css/playlist.scss'
</style>