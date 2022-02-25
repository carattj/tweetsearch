<!-- This file contains the template, script and style of each tweet. -->

<template>
  <div class="tweet">
    <div class="box">
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <b-image
                :src="profile_pic"
                :src-fallback="profile_pic_not_loaded"
              ></b-image>
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{this.full_name}}</p>
            <p class="subtitle is-6">@{{this.username}}</p>
          </div>

        </div>
        <hr>

        <div class="content">
          {{this.content}}
          <br>
          <figure>
            <b-image
              v-show="showImage"
              v-if="metadata"
              id="metadata"
              :src="metadata"
              @error="hideImage"
            ></b-image>
          </figure>
        </div>
        <hr>

        <nav class="level is-mobile">
          <div class="block">
            <button class="button is-danger is-light">
              <b-icon pack="fas" icon="heart"></b-icon>
              <span>{{this.likes}}</span>
            </button>
            <button class="button is-info is-light">
              <b-icon pack="fas" icon="retweet"></b-icon>
              <span>{{this.retweets}}</span>
            </button>

            <b-tooltip :label="longDate"
                       type="is-dark is-light"
                       position="is-bottom">
            <button class="button is-warning is-light">
              <b-icon pack="fas" icon="calendar-alt"></b-icon>
              <span><time datetime="2016-1-1">{{this.shortDate}}</time></span>
            </button>
            </b-tooltip>

            <button class="button is-info is-light" @click="openTweet">
              <b-icon pack="fab" icon="twitter"></b-icon>
              <span>See tweet</span>
            </button>

          </div>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                showImage: true,
                url:null,
                longDate:null,
                shortDate:null,
                full_name:null,
                username:null,
                profile_pic:null,
                content:null,
                metadata:null,
                likes:null,
                retweets:null,
                profile_pic_not_loaded : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/User_font_awesome.svg/1200px-User_font_awesome.svg.png",
            }
        },
        methods: {
          openTweet: function(){
            window.open(this.url,'_blank');
          },
          hideImage: function(){
            this.showImage = false;
          },
          format: function () {
            let likes = this.$props.tweet.likes;
            if(likes !== undefined){
              this.likes = likes.join();
            }else{
              this.likes = "0";
            }

            let retweets = this.$props.tweet.retweets;
            if(retweets !== undefined){
              this.retweets = retweets.join();
            }else{
              this.retweets = "0";
            }

            let metadata = this.$props.tweet.metadata;
            if(metadata !== undefined){
              this.metadata = metadata.join();
            }

            let repost = this.$props.tweet.repost;
            if(repost !== undefined){
              this.repost = repost.join();
            }

            let date = this.$props.tweet.date.join().split(" ");
            let newLongDate = date[3] + " " + date[2] + " " + date[4] + ", " + date[0] + ":" + date[1];
            let newShortDate = date[3] + " " + date[2];
            if(date[4] !== "2020"){
              newShortDate += " " + date[4]
            }
            this.url = this.$props.tweet.url.join();
            this.longDate = newLongDate;
            this.shortDate = newShortDate;
            this.full_name = this.$props.tweet.full_name.join();
            this.username = this.$props.tweet.username.join();
            this.profile_pic = this.$props.tweet.profile_pic.join();
            this.content = this.$props.tweet.content.join();
          },
        },
        created(){
          this.format();
        },
        props: ['tweet'],
    }
</script>

<style>
.tweet{
  margin: auto;
  width: 75%;
  padding: 10px;
}

#metadata{
  max-width: 55%;
  height: auto;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
  border-radius: 8px;
  border: 2px solid #ddd;
}

#metadata img{
  max-height: 350px;
}
</style>
