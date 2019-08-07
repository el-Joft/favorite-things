<template>
  <div class="add-favorite">
    <form @submit.prevent="updateFavorite">
      <div class="row" v-for="(error, index) in data_errors" :key="index">
        <div class="alert alert-danger col-md-3" role="alert">
          <p style="color:red">{{ error }}</p>
        </div>
      </div>
      <div><h2>Favorite</h2></div>
      <div class="form-group">
        <label for="title">Title</label>
        <input v-validate="'required'" name="title" type="text" class="form-control" id="title" v-model="favorite.title" aria-describedby="titleHelp" placeholder="Enter your favorite here">
        <small id="titleHelp" class="form-text text-muted">Your Favorite title</small>
        <i v-show="errors.has('title')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('title') }}</span>
      </div>
      <div class="form-group">
        <label for="descriptionId">Description</label>
        <textarea v-model="favorite.description" class="form-control" id="descriptionId" rows="3"></textarea>
      </div>
      <div class="container">
        <MetaData v-for="(i, index) in metadata" :key="index" v-model="metadata[index]"/>
        <div class="col-md-3">
          <label for="">click here to add more</label>
          <button @click="addMore" type="button" class="btn add-more btn-primary">Add more</button>
        </div>
      </div>
      <div class="form-group">
        <label for="categoryId">Category</label>
        <select v-validate="'required'" name="category" v-model="category" class="form-control" id="categoryId">
          <option :value="cat.name" v-for="cat in categories" :key="cat.id">{{ cat.name }}</option>
        </select>
        <i v-show="errors.has('category')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('category') }}</span>
      </div>
      <div class="form-group">
        <label for="rankingId">Ranking</label>
        <input v-validate="'numeric|required'" name="ranking" type="number" v-model="favorite.ranking" class="form-control" id="rankingId">
        <i v-show="errors.has('ranking')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('ranking') }}</span>
      </div>
      <button type="submit" class="btn favorite-btn btn-primary" >Submit</button>
    </form>
  </div>
</template>

<script>
import {
  ALL_CATEGORIES,
  SINGLE_FAVORITE,
  UPDATE_FAVORITE_MUTATION,
  ALL_FAVORITE_QUERY
} from '@/graphql'
import MetaData from '@/components/Favorite/MetaData'

export default {
  name: 'updateFavorite',
  components: {
    MetaData
  },
  data () {
    return {
      title: '',
      description: '',
      category: '',
      ranking: '',
      data_errors: [],
      form_error: '',
      categories: [],
      metadata: [{name: '', content: ''}],
      favorite: {category: {}},
      id: this.$route.params.id
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
    },
    categories: {
      query: ALL_CATEGORIES
    }
  },
  methods: {
    addMore () {
      this.metadata.push(JSON.stringify({name: '', content: ''}))
    },
    async updateFavorite () {
      await this.$validator.validateAll().then(result => {
        if (result) {
          this.$apollo
            .mutate({
              mutation: UPDATE_FAVORITE_MUTATION,
              variables: {
                id: this.id,
                title: this.favorite.title,
                description: this.favorite.description,
                ranking: parseInt(this.favorite.ranking),
                category: this.category.toString()
              },
              update: (store, { data: { updateFavorite } }) => {
                // read data from cache for this query
                const data = store.readQuery({ query: ALL_FAVORITE_QUERY })

                data.favorites.push(updateFavorite)

                // write data back to the cache
                store.writeQuery({ query: ALL_FAVORITE_QUERY, data })
              }
            })
            .then(response => {
              this.$router.replace('/favorites')
            })
            .catch(error => {
              this.data_errors.push(error.message.split(':')[1].trim())
              // We restore the initial user input
            })
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  form {
    font-family: 'Capriola', sans-serif;
  }
  .add-favorite {
    margin: 60px;
    width: 80%;
  }
  .md-error {
    color: #ff0000;
  }
  .favorite-btn {
    color: #ffffff!important;
    background: #307d7f!important;
    border-color: #307d7f!important;
  }
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
  .is-danger {
    color: red!important;
  }
  .add-more {
    margin-bottom: 10px;
    color: #ffffff!important;
    background: #307d7f!important;
    border-color: #307d7f!important;
  }
</style>
