<template>
  <div>
    <h2 class="section-head">
      Category Name
    </h2>
    <div class="container">
      <div class="row">
        <CatCard />
      </div>

    </div>
  </div>
</template>

<script>
import CatCard from '@/components/Favorite/Card'
export default {
  name: 'Card',
  components: {
    CatCard
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
