<template>
  <div class="container">
    <div class="section-head">
      <h2>Favorites</h2>
    </div>
    <div  v-for="favorite in favorites.slice(0, 6)" :key="favorite.id" class="row">
      <Cards :propFav="favorite"/>
    </div>
  </div>
</template>

<script>
import Cards from '@/components/Favorite/Card'

import { ALL_FAVORITE_QUERY } from '@/graphql'

export default {
  name: 'Card',
  props: {
    FavoriteObject: this.favorite
  },
  components: {
    Cards
  },
  data () {
    return {
      favorites: []
    }
  },
  apollo: {
    favorites: {
      query: ALL_FAVORITE_QUERY
    }
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
