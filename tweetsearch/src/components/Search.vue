<!-- This file contains the template, script and style of the Search page. -->

<template>
  <div id="search">
    <div id="header">
        <b-field grouped>
          <b-field>
            <b-tooltip :label="this.labelThesaurus"
                       type="is-light"
                       multilined
                       position="is-top">


              <b-field class="file is-primary" :class="{'has-name': !!file}">
                <b-upload accept="application/json" v-model="file" class="file-label">
                <span v-show="this.file == null" class="file-cta">
                    <b-icon pack="fas" class="file-icon" icon="file-upload"></b-icon>
                    <span class="file-label">Upload synonyms</span>
                </span>
                <span style="border:1px solid lightgray; border-radius: 4px" class="file-name" v-if="file">
                    {{ file.name }}
                </span>
                </b-upload>
              </b-field>

            </b-tooltip>
          </b-field>

          <b-field>

            <b-tooltip label="Remove Thesaurus"
                       type="is-light"
                       position="is-top">
              <b-button
                type="is-danger"
                outlined
                @click="removeFile"
                v-if="file"
                icon-pack="fas"
                icon-left="trash-alt">
              </b-button>
            </b-tooltip>

          </b-field>

          <b-field>
            <b-select
              v-model="filter"
              icon="filter"
              icon-pack="fas"
              >
              <option value="">No filter
              </option>
              <option value="hashtag"># Hashtag</option>
              <option value="tag">@ Tag</option>
              <option value="username">Username</option>
              <option value="full_name">Full name</option>
            </b-select>
          </b-field>
          <b-field expanded>

            <b-input
              id="input"
              placeholder="Search..."
              icon="search"
              icon-pack="fas"
              v-model="query"
            ></b-input>

          </b-field>

          <b-field >

            <p class="control">
              <button expanded @click="getQuery" class="button is-primary">Search</button>
            </p>

          </b-field>
        </b-field>

      <b-field grouped>
        <b-field expanded>
          <b-collapse class="card" animation="slide" aria-id="contentIdForA11y3" v-model="isOpen">
            <div
              slot="trigger"
              slot-scope="props"
              class="card-header"
              role="button"
              aria-controls="contentIdForA11y3">
              <p class="card-header-title">
                Emoji Keyboard
              </p>
              <a class="card-header-icon">
                <b-icon
                  pack="fas"
                  :icon="props.open ? 'window-close' : 'keyboard'">
                </b-icon>
              </a>
            </div>
            <div class="card-content">
                <div class="centerKeyboard">
                  <VEmojiPicker
                    labelSearch="Search"
                    lang="pt-BR"
                    @select="onSelectEmoji"
                  />
              </div>
            </div>
          </b-collapse>
        </b-field>
      </b-field>

      <b-field grouped>
        <b-field expanded>
          <Statistics
            v-show="this.statisticsStatus"
            :statistics="statistics"
          ></Statistics>
        </b-field>
      </b-field>

    </div>

    <div id="content">
      <Tweet
        v-if="tweet.full_name != null"
        v-for="tweet in tweets"
        v-bind:key="tweet.text"
        :tweet="tweet"
      ></Tweet>
    </div>
  </div>
</template>

<script>
import { VEmojiPicker, emojisDefault, categoriesDefault } from "v-emoji-picker";
import Tweet from "./Tweet";
import Statistics from "./Statistics";
export default {

  components: {
    Tweet,
    Statistics,
    VEmojiPicker,
    emojisDefault,
    categoriesDefault
  },

  data() {
    return {
      labelThesaurus: "You firstly have to create your synonyms thesaurus in the Thesaurus Page.",
      expanded: false,
      file: null,
      fileContent: null,
      filter: "",
      query: "",
      showDialog: false,
      endpoint: "http://localhost:8983/solr/tweets/select?q=",
      tweets: null,
      isOpen: false,
      statisticsStatus: false,
      statistics: {
        q: "empty",
        maxScore: 0,
        numFound: 0,
        QTime: 0
      }
    };
  },

  methods: {
    specialToAscii(query){
      query = query.replace(/#/g, "%23");
      query = query.replace(/@/g, "%40");
      return query;
    },
    buildEndpoint(query){

      //replace some special characters
      query = this.specialToAscii(query);

      let request = this.endpoint;

      //flag to know if the query is composed by more than one word
      let multiple_words = query.trim().split(" ").length > 1;

      //if there is a filter we want an exact match
      if(this.filter !== ""){

        //add filter name
        request += this.filter;

        if(multiple_words){

          request += "%3A" + query;

        }else{

          //exact match
          request += '%3A"' + query + '"';

        }

      //no filter
      }else{

        request += query;
      }

      //50 results
      request += "&rows=50";
      return request;
    },
    removeFile(){
      this.file = null;
      this.expanded = false;
      this.fileContent = null;
      this.labelThesaurus = "You firstly have to create your synonyms thesaurus in the Thesaurus Page.";
    },
    findSyns(word){
      let fileJson = JSON.parse(this.fileContent);
      let len = fileJson.length;
      let syns = [];
      for(let i = 0; i < len; i++){
        if(fileJson[i].includes(word)){
          syns.push(fileJson[i])
        }
      }
      syns = syns.flat();
      syns = syns.filter(function(item, pos) {
        return syns.indexOf(item) === pos;
      })
      return syns;
    },
    clearStatistics(){
      this.statisticsStatus = false;
      this.statistics = {
        q: "empty",
        maxScore: 0,
        numFound: 0,
        QTime: 0
      };
    },
    onSelectEmoji: function(emoji) {
      this.query += emoji.data;
    },
    getQuery: function() {
      this.getPost();
    },
    expandQuery: function(query){
      let words = query.split(" ");
      let expanded = [];
      for(let i = 0; i < words.length; i++){
        let output = this.findSyns(words[i]);
        if(output.length > 0){
          expanded.push(output);
        }
      }
      if(expanded.length === 0){
        this.expanded = false;
        return query;
      }
      this.expanded = true;
      return expanded.join().replace(/,/g, " ");
    },
    getPost: function() {
      if (this.query) {
        this.isOpen = false;
        this.tweets = null;
        this.statisticsStatus = true;
        this.expanded = false;

        let query;
        this.file != null ? query = this.expandQuery(this.query) : query = this.query;
        let request = this.buildEndpoint(query);
        console.log(request);
        fetch(request)
          .then(res => res.json())
          .then(res => {
            this.statistics = {
              maxScore: res.response.maxScore,
              numFound: res.response.numFound,
              QTime: res.responseHeader.QTime
            }
            this.expanded ? this.statistics.q = "expanded" : this.statistics.q = res.responseHeader.params.q;

            let data = JSON.parse(JSON.stringify(res)).response;
            if (data !== undefined) {
              this.tweets = data.docs;
            } else {
              this.tweets = null;
            }
          })
      .catch(rejected => {
            console.log(rejected);
          });
      } else {
        this.tweets = null;
        this.clearStatistics();
      }
    },
  },

  watch: {
    file: function () {
      const reader = new FileReader();
      reader.onload = e => this.$emit("load",
        this.fileContent = e.target.result
      );
      reader.readAsText(this.file);
      this.labelThesaurus = "You succesfully uploaded " + this.file.name;
    },
  }
};
</script>

<style>
#header{
  width: 60%;
  margin: auto;
}

.centerKeyboard {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 325px;
}
</style>
