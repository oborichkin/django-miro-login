<template>
  <div id="app">
    <h1>Test</h1>
    <p>{{ users }}</p>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      users: []
    }
  },
  mounted() {
    this.$axios
      .get("users/")
      .then(response => { this.users = response.data })
      .catch(error => { console.log(error) })
  }
}
</script>

