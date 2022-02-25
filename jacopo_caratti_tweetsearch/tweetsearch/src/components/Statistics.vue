<!-- This file contains the template, script and style of the Statistics Box. -->

<template>
  <div id="statistics">
      <b-collapse class="card" animation="slide" aria-id="contentIdForA11y3" v-model="isOpen">
        <div
          slot="trigger"
          slot-scope="props"
          class="card-header"
          role="button"
          aria-controls="contentIdForA11y3">
          <p class="card-header-title">
            Statistics Box
          </p>
          <a class="card-header-icon">
            <b-icon
              pack="fas"
              :icon="props.open ? 'window-close' : 'chart-bar'">
            </b-icon>
          </a>
        </div>
        <footer class="card-footer">
          <p class="card-footer-item">Query: '{{this.$props.statistics.q}}'</p>
          <p class="card-footer-item">Relevant tweets: {{this.$props.statistics.numFound}}</p>
          <p class="card-footer-item">Max tweet score: {{this.$props.statistics.maxScore}}</p>
          <p class="card-footer-item">Response time: {{this.$props.statistics.QTime}}</p>
        </footer>
      </b-collapse>
  </div>
</template>

<script>
export default {

  data() {
    return {
      isOpen: false,
    }
  },

  props: ['statistics'],
}
</script>
