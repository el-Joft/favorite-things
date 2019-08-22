// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import {
  ApolloClient
} from 'apollo-client'
import {
  HttpLink
} from 'apollo-link-http'
import {
  InMemoryCache
} from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import VeeValidate from 'vee-validate'
// import plugin
import VueToastr from 'vue-toastr'

const httpLink = new HttpLink({
  // URL to graphql server, you should use an absolute URL here
  uri: 'https://daha0htt4g.execute-api.us-east-2.amazonaws.com/dev/favorite/'
})

// create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})

// use plugin
Vue.use(VueToastr, {
  /* OverWrite Plugin Options if you need */
})

// install the vue plugin
Vue.use(VueApollo)
/* eslint-disable no-new */
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.use(VueMaterial)

Vue.use(VeeValidate)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  apolloProvider,
  components: {
    App
  },
  template: '<App/>'
})
