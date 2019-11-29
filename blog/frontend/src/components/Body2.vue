<template>
    <div class="totalidad">
        
        <div class="body">
            <div class="buscador" v-if="playVisibility==true">
            <i @click="cambiarPlay" class="fas fa-chevron-left back"></i>
            <img src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
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
            <input class="busqueda" type="text" placeholder="Realice su búsqueda">
            <section class="section">
                <h2>Destacados</h2>
                <div class="destacados">
                    <div @click="cambiarPlay" class="album">
                        <img class="imagen" src="https://images-na.ssl-images-amazon.com/images/I/71k-5WHYB9L._SX342_.jpg" alt="">
                        <label for="">Twenty One Pilots</label>
                    </div>
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
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>

                </div>
            </section>
            <section class="section">
                <h2>Albumes</h2>
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
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>

                </div>
            </section>
            <section class="section">
                <h2>Temas</h2>
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
            </section>
            <section class="section">
                <h2>Artistas</h2>
                <div class="destacados artistas">
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
            </section>
            <section class="section">
                <h2>Playlists</h2>
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
                    <div class="album">
                        <img class="imagen" src="https://nuevaya.com.ni/wp-content/uploads/2016/09/israel-lanuza.png" alt="">
                        <label for="">Israel Lanuza</label>
                    </div>

                </div>
            </section>
            <section class="section">
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
            </section>
        </div>
    </div>
</template>

<script>


export default {
    name:'Body2',
    data(){
        return{
            playVisibility:false
        }
    },
    methods:{
        cambiarPlay(){
            this.playVisibility=!this.playVisibility;
        },
        artista(){
            this.$router.replace('/artista');
        },
        album(){
            this.$router.replace('/album');
        }
    }

}
</script>

<style scoped>
    @import '../css/body2.scss';
</style>