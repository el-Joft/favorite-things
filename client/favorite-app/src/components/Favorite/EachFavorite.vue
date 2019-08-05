<template>
  <div>
    <h2 class="section-head">
      Favorite
    </h2>
    <div class="row" v-for="(error, index) in data_errors" :key="index">
      <div class="alert alert-danger col-md-3" role="alert">
        <p style="color:red">{{ error }}</p>
      </div>
    </div>
    <div class="container">
        <p>Title</p>
        <h2>
          {{ favorite.title }}
        </h2>
        <hr>
      <p>Description</p>
        <h5>{{ favorite.description }}</h5>
      <hr>
    <p>Ranking</p>
    <h5>{{ favorite.ranking }}</h5>
      <hr>
      <div v-for="metad in favorite.metadataSet" :key="metad.id" class="row">
        <div class="col-md-4">
          <p><strong>Name:</strong> {{ metad.key }}</p>
          <p><strong>Content:</strong> {{ metad.value }}</p>
        </div>
      </div>
      <hr/>
      <p>Category</p>
      <router-link :to="`/category/${favorite.category.id}`"><h5>{{ favorite.category.name }}</h5></router-link>
      <hr>
      <p>Created Date</p>
      <h5>{{ favorite.createdAt }}</h5>
      <hr>
      <div class="row">
        <router-link :to="`/edit_favorite/${favorite.id}`"><md-button class="md-raised md-primary">Edit</md-button></router-link>
        <md-button  @click="deleteFavorite" class="delete-btn md-primary">Delete</md-button>
      </div>
  </div>
  </div>
</template>

<script>
import { SINGLE_FAVORITE,
  DELETE_FAVORITE_MUTATION } from '@/graphql'
export default {
  name: 'EachFavorite',
  data () {
    return {
      favorite: {category: {}},
      id: this.$route.params.id,
      data_errors: []
    }
  },
  apollo: {
    favorite: {
      query: SINGLE_FAVORITE,
      variables () {
        return {
          id: this.id
        }
      }
    }
  },
  methods: {
    deleteFavorite () {
      this.$apollo
        .mutate({
          mutation: DELETE_FAVORITE_MUTATION,
          variables: {
            id: this.id
          }
        })
        .then(response => {
          this.$router.replace('/add_favorite')
        })
        .catch(error => {
          this.data_errors.push(error.message.split(':')[1].trim())
        })
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
  .delete-btn {
    background-color: #ff0000;
    color: white;
  }
  .md-raised {
    background-color: #307d7f!important;
    color: #ffffff;
  }
</style>
