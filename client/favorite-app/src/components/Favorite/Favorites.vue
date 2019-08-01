<template>
  <div>
    <h2 class="section-head">
       Favorites
    </h2>
    <div class="container">
      <div class="row">
        <FavoritesCard />
      </div>

    </div>
  </div>
</template>

<script>
import FavoritesCard from '@/components/Favorite/Card'
export default {
  name: 'Card',
  components: {
    FavoritesCard
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
