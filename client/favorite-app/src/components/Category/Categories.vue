<template>
  <div>
    <div class="categories-head">
      <h2>Categories</h2>
    </div>
    <div class="container">
      <div class="row">
        <CategoryCard />
        <CategoryCard />
        <CategoryCard />
      </div>
    </div>
  </div>
</template>

<script>
import CategoryCard from '@/components/Favorite/Card'
export default {
  name: 'Card',
  components: {
    CategoryCard
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
