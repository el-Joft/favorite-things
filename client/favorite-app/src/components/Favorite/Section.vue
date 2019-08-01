<template>
  <div class="container">
    <div class="section-head">
      <h2>Favorites</h2>
    </div>
    <div class="row">
      <Cards />
      <Cards />
      <Cards />
    </div>
  </div>
</template>

<script>
import Cards from '@/components/Favorite/Card'
export default {
  name: 'Card',
  components: {
    Cards
  }
}
</script>

<style lang="scss" scoped>
  .section-head {
    text-align: center;
    padding: 40px 0;
    font-family: 'Capriola', sans-serif;
  }
</style>
