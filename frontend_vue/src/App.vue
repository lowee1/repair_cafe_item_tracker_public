<template>
  <!-- nav bar -->
  <b-navbar variant="primary">
    <div id="nav-link-container">
      <router-link to="/" class="nav">Home</router-link>
      <router-link to="/about" class="nav">About</router-link>
      <router-link to="/contact" class="nav">Contact</router-link>
    </div>
    <b-navbar-brand to="/" id="brand-text">Repair Cafe</b-navbar-brand>

  </b-navbar>

  <!-- main content -->
  <div id="main-container">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
}


</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Black+Ops+One');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  margin-top: 0;
}

#brand-text {
  font-family: 'Black Ops One', cursive;
  --bs-navbar-brand-font-size: 4vw !important;
}

:root {
  --bs-link-color: #fff !important;
}

#nav-link-container {
  display: flex;
}

.nav {
  text-decoration: none;
  margin: 0 10px;
  font-size: medium;
}

#main-container {
  display: flex;
  position: relative;
  top: var(--bs-navbar-brand-font-size);
  margin-top: 5px;
  flex-direction: column;
}

body {
  height: 100vh;
}

#item-search-form {
  display: flex;
  flex-direction: row;
}
</style>
