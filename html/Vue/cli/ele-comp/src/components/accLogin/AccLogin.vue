<template>
  <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
      <el-form-item prop="username">
        <el-input placeholder="user" v-model="ruleForm.username">
          <i slot="prefix" class="el-icon-user"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input placeholder="password" v-model="ruleForm.password" show-password>
          <i slot="prefix" class="el-icon-lock"></i>
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width: 100%" @click="login">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "AccLogin",
  component: {},
  props: {
    ruleForm: {
      type: Object,
      require: true
    },
    rules: {
      type: Object,
      require: true
    }
  },
  methods: {
    login() {
      this.$refs.ruleForm.validate((valid) => {
        if(valid) {
          this.$emit('submit')
        } else {
          this.$emit ('errHandle')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
