<template>
    <video 
    class='loop' 
    :src="src"
    alt=""
    muted
    loop
    playsinline
    autoplay
    @mouseenter=" "
    @mouseleave=""
    disablePictureInPicture></video>
</template>
<script setup>
  import { ref } from 'vue'
  const props = defineProps(['id'])

  // const src = ref('http://localhost:3000/loops/'+props.id+'/'+props.id+'.mp4')
  // const src = ref(webpack_url)

  // for testing purposes, we are using the webpack url
  const webpack_url = require(`../assets/loops/${props.id}/0-preview.mp4`)
  const src = ref(webpack_url)
  
  // console.log('src:', src.value)

  // const play = (event) => {
  //   if(event && event.target.paused ){
  //     event.target.play()
  //   }
  // }
  
  // const stop = (event) => {
  //   // console.log('stop called')
  //   if(event && !event.target.paused){
  //     event.target.pause()
  //     event.target.currentTime = 0           
  //   }
  // }
</script>
<style >
    /* dummy */
/* .container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
} */

/* .dummy {
  width: calc(33.333% - 10px);
  height: 100px;
  background-color: #42b983;
  border: 1px solid black;
  overflow: hidden;
}

.loop {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
} */
video {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  
}


</style>