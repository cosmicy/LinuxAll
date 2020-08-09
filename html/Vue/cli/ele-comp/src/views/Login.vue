<template>
  <div class="login">
    <h1>普通登录组件</h1>
    <div class="account">
      <acc-login :ruleForm="ruleForm" :rules="rules" @submit="submit" @errHandle="errHandle"></acc-login>
    </div>
    <h1>短信</h1>
    <div class="phone">
      <phoneLogin></phoneLogin>
    </div>
  </div>
</template>

<script>
export default {
name: "Login",
  components: {},
  props: {},
  data() {
    return {
      ruleForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          {
            require: true,
            message: '用户名不能为空',
            trigger: 'blur'
          },
          {
            min: 2,
            max: 6,
            message: '用户名在2-6个字符之间',
            trigger: 'blur'
          }
        ],
        password: [
          {
            require: true,
            message: '密码不能为空',
            trigger: 'blur'
          },
          {
            min: 6,
            max: 10,
            message: '密码在6-10个字符之间',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    submit() {
      this.$message.success("填写成功")
    },
    errHandle() {
      this.$message.error("表单错误")
    }
  }
}
</script>

<style scoped>
.login {
  margin-top: 30px;
  margin-left: 30px;
}
.account, .phone{
    width: 500px;
  }
</style>
