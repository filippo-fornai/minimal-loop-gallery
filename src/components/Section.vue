<template>
    <h2>
        {{ title }}
    </h2>
    
    <div v-html="html">
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';

const props = defineProps(['section', 'id']);

const title = ref('')
const html = ref('')

onMounted(()=>{
    // console.log('section:', props.section.title);
    // console.log('section:', props.section);
    title.value = props.section.title
    // console.log('id:', props.id);
    // console.log(html.value);

    for (let component of props.section.components) {
        // console.log('element:', element);
        if (component.type === 'paragraph') {
            html.value += `<div class="component-media-container">`
            html.value += `<p
                class="component-paragraph">
                ${component.content}
                </p>`
            html.value += `</div>`    
        }else if (component.type === 'video') {
            
            html.value += `<div class="component-media-container">`
            html.value += `<video 
                src="${require(`../assets/loops/${props.id}/sections_media/${component.content}.mp4`)}" 
                class="component-media"
                muted 
                loop 
                playsinline 
                autoplay 
                disablePictureInPicture>
                </video>`
            html.value += `</div>`
            
        }else if (component.type === 'image') {
            html.value += `<div class="component-media-container">`
            html.value += `<img
                class="component-media"
                src="${require(`../assets/loops/${props.id}/sections_media/${component.content}.png`)}">`
            html.value += `</div>`
        }

    }
})
</script>

<style>
.component-media-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    overflow: hidden;
    margin: 0 auto;
    max-width: 90%;
    height: 100%;
    border: 4px solid #353535;
    box-sizing: border-box;
}
.component-media {
    width: 50%;
    position:relative;
}
hr{
    border: 0;
    border-top: 2px solid #ccccccc5;
    width: 80%;
}
</style>