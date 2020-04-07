import Vue from 'vue';
import Router from 'vue-router';
import Body from '../components/Body.vue';
import Body2 from '../components/Body2.vue';
import Artista from '../components/Artista.vue';
import Album from '../components/Album.vue';
import Usuario from '../components/Usuario.vue';
import Playlist from '../components/Playlist.vue';

Vue.use(Router);

export default new Router({
    routes:[
        {
            path:'/',
            component:Body
        },
        {
            path:'/body2',
            name:'body2',
            component:Body2
        },
        {
            path:'/artista',
            name:'artista',
            component:Artista,
            props:true
        },
        {
            path:'/album',
            name:'album',
            component:Album,
            props:true
        },
        {
            path:'/usuario',
            component:Usuario
        },
        {
            path:'/playlist',
            name:'playlist',
            component:Playlist,
            props:true
        }
    ]
})