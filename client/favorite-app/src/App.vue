<template>
  <div id="app">
    <nav class="navbar navbar-light bg-light">
      <router-link class="navbar-brand logo" to="/">Favorite</router-link>
      <ul class="nav nav-class justify-content-end">
        <li class="nav-item">
          <router-link class="nav-link active" to="/">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" to="/categories">Categories</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" to="/favorites">Favorites</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" to="/add_favorite">Add Favorite</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link active" to="/audit_logs"> Audit Logs</router-link>
        </li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  body {
    margin: 0;
  }
  .bg-light {
    background-color: #ffffff!important;
    height: 100px;
  }
  .nav-class {
    font-family: 'Capriola', sans-serif;
    margin-right: 100px;
  }
  .nav-class a {
    color:  #307d7f;
  }
  .logo {
    font-family: 'Fredoka One', cursive;
    font-size: 25px;
    color: #454444;
    margin: 10px 10px 10px 50px;
  }
</style>
