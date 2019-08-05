<template>
  <div class="row">
      <div class="col-md-4">
        <div class="form-group">
          <label for="metadata">More Data</label>
          <input type="text" ref="name" name="name" class="form-control" @input="handleInput" :value="$attrs.value.name" id="metadata" placeholder="more favorite">
        </div>
      </div>
      <div>
        <div class="form-group">
          <label for="type">Content Type</label>
          <select ref="type" v-validate="'required'" @change="handleInput" name="type" class="form-control" id="type" >
            <option value="text">text</option>
            <option value="number">number</option>
            <option value="date">date</option>
            <option value="enums">enums</option>
          </select>
          <i v-show="errors.has('type')" class="fa fa-warning"></i>
          <span class="help is-danger">{{ errors.first('type') }}</span>
        </div>
      </div>
    <div class="col-md-4">
      <div class="form-group">
        <label for="content">Content</label>
        <input :type="$attrs.value.type" v-validate="'required'" ref="content" name="content" :value="$attrs.value.content" @input="handleInput" :disabled="!$attrs.value.name" class="form-control" id="content" />
      </div>
      <span style="color: red" v-show="errors.has('content')" class="help is-danger">{{ errors.first('content') }}</span>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handleInput () {
      const r = {
        [this.$refs.name.name]: this.$refs.name.value,
        [this.$refs.content.name]: this.$refs.content.value,
        [this.$refs.type.name]: this.$refs.type.value
      }
      this.$emit('input', r)
    }
  }
}
</script>
