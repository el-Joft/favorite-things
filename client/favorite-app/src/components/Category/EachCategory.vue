<template>
  <div>
    <md-table v-model="searched" md-sort="name" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Favorite</h1>
        </div>

        <md-field md-clearable class="md-toolbar-section-end">
          <md-input placeholder="Search by name..." v-model="search" @input="searchOnTable" />
        </md-field>
      </md-table-toolbar>
      <md-table-empty-state
        md-label="No Favorite found"
        :md-description="`No Favorite found for this '${search}' query. Try a different search term or create a new Favorite.`">
        <router-link to="/add_favorite"><md-button class="md-primary md-raised">Create New Favorite</md-button></router-link>
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="Ranking" md-sort-by="id" md-numeric>{{ item.ranking }}</md-table-cell>
        <md-table-cell md-label="Title" md-sort-by="Title"><router-link :to="`/favorite/${item.id}`">{{ item.title }}</router-link></md-table-cell>
        <md-table-cell md-label="Description" md-sort-by="Description">{{ item.description }}</md-table-cell>
        <md-table-cell md-label="Metadata" md-sort-by="Metadata">Metadata</md-table-cell>
        <md-table-cell md-label="Created Date" md-sort-by="title">{{ item.createdAt }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>

import { SINGLE_CATEGORY } from '@/graphql'
const toLower = text => {
  return text.toString().toLowerCase()
}

const searchByName = (items, term) => {
  if (term) {
    console.log(items.filter(item => toLower(item.title).includes(toLower(term))))
    return items.filter(item => toLower(item.title).includes(toLower(term)))
  }
  return items
}

export default {
  name: 'EachCategory',
  data () {
    return {
      category: {favorite: []},
      favorite: [],
      id: this.$route.params.id,
      search: null,
      searched: []
    }
  },
  apollo: {
    // fetch category by ID
    category: {
      query: SINGLE_CATEGORY,
      variables () {
        return {
          id: this.id
        }
      },
      update (data) {
        this.searched = data.category.favorite
        return data.category
      }
    }
  },
  methods: {
    newUser () {
      window.alert('Noop')
    },
    searchOnTable () {
      this.searched = searchByName(this.category.favorite, this.search)
    }
  },
  created () {
    this.searched = this.category.favorite
  }
}
</script>

<style lang="scss" scoped>
  .section-head {
    text-align: center;
    padding: 40px 0;
    font-family: 'Capriola', sans-serif;
  }
  .md-field {
    max-width: 300px;
  }
</style>
