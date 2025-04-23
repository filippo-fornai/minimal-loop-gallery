<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
body {
  margin: 0;
  padding: 0;
  background: #161a1d;
  color: white;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
}

nav {
  padding: 30px;
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.5);
  margin : 0 0 30px 0;
}

nav a {
  font-weight: bold;
  color:rgba(255, 255, 255, 0.534);
  text-decoration: none;
  border: 1px solid white;
  padding: 5px 10px;
  border-radius: 10px;
  transition: all 0.1s ease-in-out;
}

nav a.router-link-exact-active {
  color:white
}

nav a:hover {
  color: white;
  background-color: rgba(255, 255, 255, 0.2);
  transition: all 0.1s ease-in-out;
}
</style>
