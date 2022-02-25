<!-- This file contains the template, script and style of the Thesaurus page. -->

<template>
  <div id="thesaurus">
      <b-field v-if="dict.length > 0">
        <b-button
          expanded
          icon-pack="fas"
          icon-left="file-download"
          @click="createJsonFile"
          type="is-success">
          Download your synonyms thesaurus
        </b-button>
      </b-field>
    <b-field grouped>

      <b-field expanded>
        <b-taginput
          placeholder="Add synonyms"
          v-model="current_syns">
        </b-taginput>
      </b-field>

      <b-field v-if="current_syns.length > 1">

        <p class="control">
          <button expanded @click="newVoice" class="button is-primary">Create synonym set</button>
        </p>

      </b-field>
      <b-field v-if="current_syns.length <= 1">
        <b-tooltip label="Enter at least two synonyms in the field on the left."
                   type="is-light"
                   multilined
                   position="is-top">

        <p class="control">
          <button disabled expanded @click="" class="button is-primary">Create synonym set</button>
        </p>
        </b-tooltip>

      </b-field>

    </b-field>
    <div id="syn_list" v-for="list in this.dict">
      <b-field>
        <b-select
          expanded
          multiple
          v-model="dict"
          native-size="2">
          <option v-for="word in list" disabled>{{word}}</option>
        </b-select>
      </b-field>
    </div>
  </div>
</template>

<script>
import { saveAs } from 'file-saver';

export default {

  data() {
    return {
      current_syns: [],
      dict: []
    };
  },

  methods: {
    createJsonFile(){
      let blob = new Blob([JSON.stringify(this.dict)], {type: "application/json"});
      saveAs(blob, "synonyms.json");
    },
    newVoice(){
      this.dict.push(this.current_syns);
      this.current_syns = [];
    }
  },
}
</script>

<style>
#thesaurus{
  margin: auto;
  width: 75%;
  padding: 10px;
}

#thesaurus h1{
  font-size: 30px;
}

#syn_list{
  margin: 30px 0;
}
</style>
