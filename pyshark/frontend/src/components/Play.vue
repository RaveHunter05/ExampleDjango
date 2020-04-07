<template>
    <div>
        <div class="iconos">
                <i class="fas fa-ellipsis-h noplay"></i>
                <i class="fas fa-step-backward noplay"></i>
                <i v-if="reproduction==true" @click="repro()" class="fas fa-play play"></i>
                <i v-if="reproduction==false" @click="pausar()" class="fas fa-pause play"></i>
                <i class="fas fa-step-forward noplay"></i>
                <i class="far fa-heart noplay"></i>
            </div>
    </div>
</template>

<script>
export default {
    name:'play',
    data(){
        return{
            contador:1,
            reproduction:true,
        }
    },
    methods:{
        repro(){
            try {
                this.cancionInicial.play()
                this.reproduction=!this.reproduction
            } catch (error) {
                alert(error)
            }
        },
        pausar(){
             try {
                this.cancionInicial.pause()
                this.reproduction=!this.reproduction
            } catch (error) {
                alert(error)
            }
        }
    },
    props:[
        'cancion'
    ],
    computed:{
        cancionInicial(){
            if(this.cancion){
            let reproducir=new Audio(this.cancion);
                return reproducir
            }else{
                return null
            }
        }
    }
}
</script>

<style lang='scss' scoped>
    @import '../css/play.scss'
</style>