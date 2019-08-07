<template>
  <div class="add-favorite">
    <div class="row" v-for="(error, index) in data_errors" :key="index">
      <div class="alert alert-danger col-md-3" role="alert">
        <p style="color:red">{{ error }}</p>
      </div>
    </div>
    <form @submit.prevent="createCategory">
      <div class="form-group">
        <label for="name">Category Name</label>
        <input v-validate="'required'" name="name" type="text" class="form-control" id="name" v-model="name"  aria-describedby="nameHelp" placeholder="Enter your category here">
        <small id="titleHelp" class="form-text text-muted">Category Title</small>
        <i v-show="errors.has('name')" class="fa fa-warning"></i>
        <span class="help is-danger">{{ errors.first('name') }}</span>
      </div>
      <button type="submit" class="btn favorite-btn btn-primary" >Submit</button>
    </form>
  </div>
</template>

<script>
import {
  CREATE_CATEGORY_MUTATION,
  ALL_CATEGORIES
} from '@/graphql'

export default {
  name: 'createCategory',
  data () {
    return {
      name: '',
      data_errors: []
    }
  },
  methods: {
    async createCategory () {
      await this.$validator.validateAll().then(result => {
        if (result) {
          this.$apollo
            .mutate({
              mutation: CREATE_CATEGORY_MUTATION,
              variables: {
                name: this.name
              },
              update: (store, { data: { createCategory } }) => {
                const data = store.readQuery({ query: ALL_CATEGORIES })

                data.categories.push(createCategory)
                store.writeQuery({ query: ALL_CATEGORIES, data })
              }
            })
            .then(response => {
              this.$router.replace('/categories')
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
