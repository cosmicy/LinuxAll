<template>
  <div>
    <el-button type = 'primary' @click="goTo('/BackTopOne')">去往页面1</el-button>
    <el-button type = 'primary' @click="goTo('/BackTopTwo')">去往页面2</el-button>
    <el-button type = 'primary' @click="goTo('/Login')">登录</el-button>
    <el-button type = 'primary' @click="goTo('/Book')">图书</el-button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
  methods: {
    goTo(path) {
      this.$router.push(path)
    }
  }
}
</script>
