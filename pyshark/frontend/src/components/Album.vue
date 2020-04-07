<template>
  <div class="body">
      <div class="principal1">
         <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
            <img :src="this.imagen" alt="">
            <h3>{{this.titulo}}</h3>
            <label>
              {{this.registro}}
            </label>

        <div class="iconos">
          <i class="fas fa-ellipsis-h pointer"></i>
          <button class="btn pointer">
            Reproducir 
          </button>
          <i class="far fa-heart pointer"></i>
        </div>
        <label for="" v-show="latrue==true">
          {{this.registroCanciones}}
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
          <td @click="enviarCancion(cancion.sonido)" >{{cancion.titulo}}</td>
          <td>{{cancion.duracion  }}</td>
          <td v-if="cancion.corazon==true"><i class="fas fa-heart pointer1"></i></td>
          <td v-if="cancion.corazon==false"><i class="far fa-heart pointer1"></i></td>
          <td><i class="fas fa-ellipsis-h pointer1"></i></td>
        </tr>
        </tbody>
      </table>
      </div>
    <Play :cancion="this.pasarCancion"/>

    </div>
  </div>
</template>

<script>

import Play from './Play';

export default {
  name:'Album',
  data(){
    return{
      cantanteAlbum:[],
      artista:'',
      contador:[],
      cancionAlbum:[],
      canciones:[],
      contadorCanciones:[],
      latrue:false,
      pasarCancion:''
    }
  },
  components:{
    Play
  },
  methods:{
    cambiarPlay(){
      this.$router.replace('/body2');
    },
    devolverNombre(){
      // this.cantanteAlbum=JSON.parse(JSON.stringify(this.cantanteAlbum))
        this.contador=this.cantanteAlbum.filter(d=>d.album.id==this.idAlbum);
        this.artista=this.contador[0]["cantante"]["nombre_artistico"];
    },
    devolverCanciones(){
      this.contadorCanciones=this.cancionAlbum.filter(d=>d.album.id==this.idAlbum);
      for(const i in this.contadorCanciones){
        this.canciones.push(this.contadorCanciones[i]['cancion'])
      }
    },
    fetchCantanteAlbum(){
       const t=this;
      fetch("http://127.0.0.1:8000/api/v1.0/cantante_album_mixin/")
        .then(response => response.json())
        .then((res)=>{
          t.cantanteAlbum=JSON.parse(JSON.stringify(res));
          return t.cantanteAlbum
      })
    },
    fetchCancionAlbum(){
       const t=this;
      fetch("http://127.0.0.1:8000/api/v1.0/cancion_album_mixin/")
        .then(response => response.json())
        .then((res)=>{
          t.cancionAlbum=JSON.parse(JSON.stringify(res));
          return t.cancionAlbum
      })
    },
    enviarCancion(dato){
      this.pasarCancion=dato;
      // alert('tu gfaxd')
    }
    // nombreArtista(){
    //   // for(i in this.cantanteAlbum){
    //   //   if(this.cantanteAlbum[i].album.id==this.idAlbum){
    //   //     this.artista=this.cantanteAlbum[i].cantante.nombre_artistico
    //   //   }
    //   // }
    //   for(var i=0; i<=this.cantanteAlbum.length;i++){
    //     this.contador+=1
    //   }
    // }
  },
  props:[
    'imagen',
    'titulo',
    'idAlbum'
  ],
  created(){
    this.fetchCantanteAlbum();
    this.fetchCancionAlbum();
    
  },
  computed:{
    registro(){
      // this.contador=this.cantanteAlbum.filter(d=>d.cantante.id==this.idAlbum)
      // return arr1[0].cantante.id

          if(this.cantanteAlbum!=''){
            this.devolverNombre()
            return this.artista
        }else{
          return 'este album no tiene artista asignado'
        }

    },
    registroCanciones(){
      if(this.cancionAlbum!=''){
        this.devolverCanciones();
        return this.canciones
      }else{
        return 'este album no cuenta con canciones'
      }
    }
  }

}
</script>

<style lang="scss" scoped>
  @import '../css/Album.scss'
</style>