<template>
  <div v-if="name">
    <div class="loop-detail-intro">
      <h1>{{ name }}</h1>
      <div class='div-loop'>
        <video 
        :src="src"
        alt=""
        muted
        loop
        playsinline
        autoplay
        disablePictureInPicture></video>  
      </div>
    </div>
    <div class="container">
      <div class="details">
      <div v-for="section in sections" :key="section.id">
        <Section :section="section" :id="id"/>
      </div>
    </div>
    
    <div class="links">
        <h2>Downloads</h2>
        <!-- <img src="../../public/blender_files/a.png" alt=""> -->
        <a class="details-link" :href="url_blender" download="loop.zip">Blender File</a>
        <a class="details-link" :href="url_mp4" download="loop.mp4">MP4 File</a>
        <!-- <a class="details-link" :href="url_gif" download="loop.gif">GIF File</a> -->
    </div>

    </div>
    
    
  </div>
  <p v-else>Loading...</p>

</template>

<script setup>
import { ref } from "vue";
import Section from "../components/Section.vue";

const props = defineProps(["id"]);
const name = ref("");
const sections = ref([]);
const src = ref("");
const url_blender = ref("");
const url_mp4 = ref("");
const url_gif = ref("");

url_blender.value = `/blender_files/${props.id}.zip`;
console.log("url_blender:", url_blender.value);

import(`../assets/loops/${props.id}/0.mp4`).then((image) => {
  url_mp4.value = image.default;
}).catch((error) => {
  console.error("Error loading image file:", error);
});

// import(`../assets/loops/${props.id}/0.gif`).then((image) => {
//   url_gif.value = image.default;
// }).catch((error) => {
//   console.error("Error loading image file:", error);
// });

import(`../assets/loops/${props.id}/0.mp4`).then((video) => {
  src.value = video.default;
}).catch((error) => {
  console.error("Error loading video file:", error);
});

import(`../assets/loops/${props.id}/data.json`)
  .then((data) => {
    name.value = data.name;
    sections.value = data.sections;
  })
  .catch((error) => {
    console.error("Error loading JSON file:", error);
  });
</script>

<style lang="css">
.loop-detail-intro {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 10px solid #353535;
}

h1{
  font-size: 2rem;
  margin: 0;
  padding: 0;
}

.div-loop {
  
  position: relative;
  width:50%;
  box-sizing: border-box;
  aspect-ratio: 16/9;
  padding: 10px;
  overflow: hidden;
  border: 3px solid #353535;
}
video{
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.details{
  position:relative;
  /* background: rgb(191, 201, 176); */
  width: 70%;
  vertical-align: top;
  border: 4px solid #353535;

}

.links{
  padding:20px;
  box-sizing: border-box;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;

  width: 30%;
  /* background: #a88f8f; */
  vertical-align: top;
  border: 4px solid #353535;

}

.container{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  margin: 0 auto;
  width: 100%;
}

.details-link{
  text-decoration: none;
  color: #ffffff98;
  border: 1px solid ;
  padding : 5px;
  text-align: center;
  width: 40%;
  background-color: #353535;
  border-radius: 10px;

  transition: all 0.3s ease-in-out;
}

.details-link:hover{
  background-color: #ffffff57;
  color: white;
  transition: all 0.3s ease-in-out;
}
</style>

