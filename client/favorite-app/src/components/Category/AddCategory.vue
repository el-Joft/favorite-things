<template>
  <div class="add-category">
    <form novalidate class="md-layout" @submit.prevent="validateUser">
      <md-card class="md-layout-item md-size-75 md-small-size-100">
        <md-card-header>
          <div class="md-title">Create Category</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('categoryName')">
                <label for="category-name">Category Name</label>
                <md-input name="category-name" id="category-name" autocomplete="given-name" v-model="form.categoryName" :disabled="sending" />
                <span class="md-error" v-if="!$v.form.categoryName.required">The Category name is required</span>
                <span class="md-error" v-else-if="!$v.form.categoryName.minlength">Invalid Category name</span>
              </md-field>
            </div>
          </div>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending">Create Category</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="categorySaved">The Category was saved with success!</md-snackbar>
    </form>
  </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import {
  required,
  minLength
} from 'vuelidate/lib/validators'

export default {
  name: 'FormValidation',
  mixins: [validationMixin],
  data: () => ({
    form: {
      categoryName: null
    },
    categorySaved: false,
    sending: false,
    lastUser: null
  }),
  validations: {
    form: {
      categoryName: {
        required,
        minLength: minLength(3)
      }
    }
  },
  methods: {
    getValidationClass (fieldName) {
      const field = this.$v.form[fieldName]

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        }
      }
    },
    clearForm () {
      this.$v.$reset()
      this.form.categoryName = null
    },
    saveUser () {
      this.sending = true

      // Instead of this timeout, here you can call your API
      window.setTimeout(() => {
        this.lastUser = `${this.form.categoryName} ${this.form.categoryName}`
        this.userSaved = true
        this.sending = false
        this.clearForm()
      }, 1500)
    },
    validateUser () {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.saveUser()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  form {
    font-family: 'Capriola', sans-serif;
  }
  .add-category {
    text-align: center;
    margin-left: 250px;
    margin-top: 40px;
  }
  .md-error {
    color: #ff0000;
  }
  .md-primary {
    color: #ffffff!important;
    background: #307d7f!important;
  }
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
</style>
