<template>
  <div class="add-favorite">
    <form>
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title" aria-describedby="titleHelp" placeholder="Enter your favorite here">
        <small id="titleHelp" class="form-text text-muted">Your Favorite title</small>
      </div>
      <div class="form-group">
        <label for="descriptionId">Description</label>
        <textarea class="form-control" id="descriptionId" rows="3"></textarea>
      </div>

      <div class="form-group">
        <label for="categoryId">Category</label>
        <select class="form-control" id="categoryId">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </select>
      </div>
      <div class="form-group">
        <label for="rankingId">Ranking</label>
        <input type="number" class="form-control" id="rankingId">
      </div>
      <button type="submit" class="btn favorite-btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import {
  required,
  email,
  minLength,
  maxLength
} from 'vuelidate/lib/validators'

export default {
  name: 'FormValidation',
  mixins: [validationMixin],
  data: () => ({
    form: {
      title: null,
      description: null,
      gender: null,
      age: null,
      email: null
    },
    userSaved: false,
    sending: false,
    lastUser: null
  }),
  validations: {
    form: {
      title: {
        required,
        minLength: minLength(3)
      },
      age: {
        required,
        maxLength: maxLength(3)
      },
      gender: {
        required
      },
      email: {
        required,
        email
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
      this.form.title = null
      this.form.description = null
      this.form.age = null
      this.form.gender = null
      this.form.email = null
    },
    saveUser () {
      this.sending = true

      // Instead of this timeout, here you can call your API
      window.setTimeout(() => {
        this.lastUser = `${this.form.title} ${this.form.description}`
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
</style>
