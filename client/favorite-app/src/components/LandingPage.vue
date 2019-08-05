<template>
  <div>
  <div class="jumbotron">
    <h1 class="display-4">Manage your Favorites</h1>
    <p class="lead">My favorite way to blow off steam is to sing obnoxiously loud in the shower.</p>
    <div class="jumbotron-btn">
      <router-link to="/add_favorite"><md-button class="md-raised md-primary">Create Favorite</md-button></router-link>
      <router-link to="/add_category"><md-button class="md-raised md-primary">Create Category</md-button></router-link>
    </div>
  </div>
  <div class="section">
    <Section/>
  </div>
    <div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Section from '@/components/Favorite/Section'
import Footer from '@/components/Favorite/Footer'

export default {
  name: 'LandingPage',
  components: {
    Section,
    Footer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
  small {
    display: block;
  }
  .jumbotron {
    font-family: 'Roboto Slab', serif;
    font-size: 20px!important;
    height: 500px;
    background-image: url('https://image.freepik.com/free-photo/interior-living-room-with-wooden-table-lamps-armchair-white-background-3d-rend_41470-44.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
  }
  .jumbotron h1 {
    font-size: 40px;
    margin: 40px;
  }
  .jumbotron p {
    font-size: 15px;
    margin: 40px;
  }
  .jumbotron-btn {
    margin: 40px;
    padding-top: 60px;
    color: #307d7f!important;
  }
  .md-raised {
    background-color: #307d7f!important;
    color: #ffffff;
  }
  .section {
    margin-bottom: 40px;
  }
</style>
