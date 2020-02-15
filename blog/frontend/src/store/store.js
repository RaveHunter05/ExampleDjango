import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        message:'Hola hijos de pvta :v',
        count:0,
        header:1
    },
    mutations:{ //here you have syncronous functions
        increment(state,payload){
            state.count+=payload;
        }
    },
    actions:{ //here you have asyncronous functions

    },
    modules:{

    }
})