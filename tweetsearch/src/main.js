// This file contains the routes of the web app

import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'

// components
import Search from './components/Search.vue'
import Credits from './components/Credits.vue'
import Thesaurus from './components/Thesaurus.vue'

// style library
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.use(Buefy)
Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name:'search',
      component: Search,
    },
    {
      path: '/credits',
      name:'credits',
      component: Credits,
    },
    {
      path: '/thesaurus',
      name:'thesaurus',
      component: Thesaurus,
    },
  ]
});

new Vue({
  el: '#app',
  render: h => h(App),
  router
});
