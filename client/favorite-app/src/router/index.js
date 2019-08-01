import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'
import EachCategory from '@/components/Category/EachCategory'
import AddCategory from '@/components/Category/AddCategory'
import Categories from '@/components/Category/Categories'
import Favorites from '@/components/Favorite/Favorites'
import Favorite from '@/components/Favorite/EachFavorite'
import AddFavorite from '@/components/Favorite/AddFavorite'
import AuditLog from '@/components/Audit/AuditLog'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/category',
      name: 'EachCategory',
      component: EachCategory
    },
    {
      path: '/add_category',
      name: 'AddCategory',
      component: AddCategory
    },
    {
      path: '/favorites',
      name: 'Favorites',
      component: Favorites
    },
    {
      path: '/add_favorite',
      name: 'AddFavorite',
      component: AddFavorite
    },
    {
      path: '/favorite/:id',
      name: 'Favorite',
      component: Favorite
    },
    {
      path: '/categories',
      name: 'Categories',
      component: Categories
    },
    {
      path: '/audit_logs',
      name: 'AuditLog',
      component: AuditLog
    }
  ]
})
