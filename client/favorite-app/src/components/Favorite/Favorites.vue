<template>
  <div>
    <h2 class="section-head">
       Favorites
    </h2>
    <div class="container">
      <div class="row" v-for="favorite in favorites" :key="favorite.id">
        <FavoritesCard :propFav="favorite"/>
      </div>

    </div>
  </div>
</template>

<script>
import FavoritesCard from '@/components/Favorite/Card'
import { ALL_FAVORITE_QUERY } from '@/graphql'

export default {
  name: 'Card',
  mounted () { },
  props: {
    FavoriteObject: this.favorite
  },
  components: {
    FavoritesCard
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
