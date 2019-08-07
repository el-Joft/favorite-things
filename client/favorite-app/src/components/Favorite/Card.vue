<template>
  <div class="card-m col-md-4">
    <div v-if="propCat">
      <md-card md-with-hover>
        <md-ripple>
          <md-card-header>
            <div class="md-title">{{ propCat.name }}</div>
            <div class="md-subhead"></div>
          </md-card-header>
          <md-card-content>
            Number of Favorite:
            {{ propCat.favorite.length }}
          </md-card-content>

          <md-card-actions>
            <router-link :to="`/category/${propCat.id}`"><md-button class="btn-card">View</md-button></router-link>
          </md-card-actions>
        </md-ripple>
      </md-card>
    </div>
    <md-card md-with-hover v-else>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{ propFav.title }}</div>
          <div class="md-subhead"><span>Ranking: </span>  {{ propFav.ranking }}</div>
        </md-card-header>
        <md-card-content>
          <span>Description: </span> {{ propFav.description }}
        </md-card-content>
        <md-card-content>
          <span>Category: </span><router-link :to="`/category/${propFav.category.id}`"> {{ propFav.category.name }}</router-link>
        </md-card-content>

        <md-card-actions>
          <router-link :to="`/favorite/${propFav.id}`"><md-button class="btn-card">View</md-button></router-link>
        </md-card-actions>
      </md-ripple>
    </md-card>
  </div>
</template>

<script>
export default {
  props: {
    // type, required and default are optional, you can reduce it to 'options: Object'
    propCat: { type: Object },
    propFav: { type: Object }
  }
}
</script>

<style>
  .card-m {
    font-family: 'Crimson Pro', serif;
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .btn-card {
    color: #ffffff;
    background-color: #307d7f;
  }
</style>
