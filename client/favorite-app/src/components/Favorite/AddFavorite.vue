<template>
  <div class="add-favorite">
    <form @submit.prevent="createFavorite">
      <div class="row" v-for="(error, index) in data_errors" :key="index">
        <div class="alert alert-danger col-md-3" role="alert">
          <p style="color:red">{{ error }}</p>
        </div>
      </div>
      <div class="form-group">
        <label for="title">Title</label>
        <input v-validate="'required'" name="title" type="text" class="form-control" id="title" v-model="title"  aria-describedby="titleHelp" placeholder="Enter your favorite here">
        <small id="titleHelp" class="form-text text-muted">Your Favorite title</small>
        <i v-show="errors.has('title')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('title') }}</span>
      </div>
      <div class="form-group">
        <label for="descriptionId">Description</label>
        <textarea v-model="description" class="form-control" id="descriptionId" rows="3"></textarea>
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
        <input v-validate="'numeric|required'" name="ranking" type="number" v-model="ranking" class="form-control" id="rankingId">
        <i v-show="errors.has('ranking')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('ranking') }}</span>
      </div>
      <button type="submit" class="btn favorite-btn btn-primary" >Submit</button>
    </form>
  </div>
</template>

<script>
import {
  CREATE_FAVORITE_MUTATION,
  ALL_CATEGORIES,
  ALL_FAVORITE_QUERY
} from '@/graphql'
import MetaData from '@/components/Favorite/MetaData'

export default {
  name: 'createFavorite',
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
      metadata: [{name: '', content: ''}]
    }
  },
  apollo: {
    categories: {
      query: ALL_CATEGORIES
    }
  },
  methods: {
    addMore () {
      this.metadata.push(JSON.stringify({name: '', content: ''}))
    },
    async createFavorite () {
      const newData = this.metadata.map(item => JSON.stringify(item))
      await this.$validator.validateAll().then(result => {
        if (result) {
          this.$apollo
            .mutate({
              mutation: CREATE_FAVORITE_MUTATION,
              variables: {
                title: this.title,
                description: this.description,
                metadata: newData,
                ranking: parseInt(this.ranking),
                category: this.category.toString()
              },
              update: (store, { data: { createFavorite } }) => {
                // read data from cache for this query
                const data = store.readQuery({ query: ALL_FAVORITE_QUERY })

                // add new post from the mutation to existing posts
                data.favorites.push(createFavorite)

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
              // this.newFavorite = newFavorite;
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
