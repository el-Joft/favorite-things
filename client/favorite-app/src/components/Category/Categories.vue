<template>
  <div>
    <div class="categories-head">
      <h2>Categories</h2>
    </div>
    <div class="container">
      <div class="row" v-for="category in categories" :key="category.id">
        <CategoryCard :propCat="category"/>
      </div>
    </div>
  </div>
</template>

<script>
import CategoryCard from '@/components/Favorite/Card'
import { ALL_CATEGORIES } from '@/graphql'

export default {
  name: 'Card',
  mounted () { },
  props: {
    categoryObject: this.category
  },
  components: {
    CategoryCard
  },
  data () {
    return {
      categories: []
    }
  },
  apollo: {
    categories: {
      query: ALL_CATEGORIES
    }
  }
}
</script>

<style lang="scss" scoped>
  .categories-head {
    text-align: center;
    padding: 40px 0;
    font-family: 'Capriola', sans-serif;
  }
</style>
