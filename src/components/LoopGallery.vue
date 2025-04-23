<template>
    <div class="loop-gallery">
            <div class='gallery-item' v-for="i in galleryLength" :key="i" >
                <router-link :to="{ name: 'loop', params: { id: i } }">
                    <Loop :id="i"/>
                </router-link>

            </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import Loop from '@/components/Loop.vue';
import { ref } from 'vue';

const galleryLength = ref(0);

import(`../assets/loops/counter.json`)
    .then((data) => {
        galleryLength.value = data.counter;
    })
    .catch((error) => {
        console.error("Error loading JSON file:", error);
    });

</script>

<style>
.loop-gallery{
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(400px, 2fr));
    padding: 15px;
}

/* a{
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    display: block;
} */

.gallery-item {
    position: relative;
    aspect-ratio: 16/9;
    box-shadow: 0 0 3px rgba(255, 255, 255, 0.5);
    overflow: hidden;
    border: 2px solid #353535;
    padding: 20px;
    transform: scale(1) 0.4s ease-in-out;
    transition: transform 0.3s ease-in-out;

}

@keyframes shadow {
    0% {
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
    50% {
        box-shadow: 0 0 10px rgba(255, 255, 255, 1);
    }
    100% {
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
    }
}

.gallery-item:hover {
    animation: shadow 1s ease-in-out infinite;
    transform: scale(1.02);
}
</style>