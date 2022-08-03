<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>你好，{{ username }}</h2>
    <el-button @click="logout">注销</el-button>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data () {
    return {
      username: '',
      msg: 'Welcome to My App'
    }
  },
  methods: {
    logout () {
      this.$http.post('/lg/logout/', this.username)
        .then(function (response) {
          if (response.data === '注销成功') {
            alert('注销成功')
            window.sessionStorage.removeItem('username')
            window.location.href = '/login'
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getUser () {
      this.username = window.sessionStorage.getItem('username')
    }
  },
  mounted () {
    this.$nextTick(function () {
      console.log(window.sessionStorage.getItem('username'))
      this.getUser()
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
