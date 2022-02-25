<!-- This file contains the template, script and style of the Credits page. -->

<template>
  <div id="credits">

    <div id="inner">
      <img id="me" src="./../assets/me.png" />
      <br>
      <br>
      <br>
      <p>Hello everyone!</p>
      <br>
      <p>My name is Jacopo Caratti and I'm attending the third year of Informatics Science at USI.</p>
      <p>For the course of Information Retrieval I had to create this project: a search engine of tweets, able to search for emojis and expand queries through given synonyms.</p>
      <br>
      <br>
      <p><i>December 10, 2020</i></p>
    </div>

  </div>
</template>

<style>

#me {
  float:left;
  margin-right: 50px;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 400px;
}

#credits h1{
  font-size: 30px;
}

#inner {
  display: table;
  margin: auto;
}

#credits {
  width: 100%
}
</style>
