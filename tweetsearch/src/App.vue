<!-- This file contains the template, script and style of the menu. -->

<template>
  <div id="app">
    <b-sidebar
      type="is-light"
      :fullheight="fullheight"
      :fullwidth="fullwidth"
      :overlay="overlay"
      :right="right"
      v-model="open"
    >
      <div>
        <img src="./assets/twitter.png" alt="tweetsearch logo">
        <b-menu id="menu">
          <b-menu-list label="Menu">
            <router-link to="/">Search</router-link>
            <router-link to="/thesaurus">Thesaurus</router-link>
            <router-link to="/credits">Credits</router-link>
          </b-menu-list>
        </b-menu>
      </div>
    </b-sidebar>
    <div id="container">
      <b-button
        icon-left="bars"
        icon-pack="fas"
        size="is-medium"
        @click="open = true">
        Menu
      </b-button>
      <img class="center" src="./assets/tweetsearch_logo.png" alt="">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import twitter from './assets/twitter.png'

  export default {

    data() {
      return {
        open: false,
        overlay: false,
        fullheight: true,
        fullwidth: false,
        right: true,
        src: twitter
      };
    }

  };
</script>

<style>
  #container{
    margin: 50px 100px 0 100px;
  }

  #menu{
    position:absolute;
  }

  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 500px;
    padding: 0 50px 50px 50px;
  }
</style>
