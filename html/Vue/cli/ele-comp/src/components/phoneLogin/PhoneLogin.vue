<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
            <el-form-item prop="phone">
                <el-input placeholder="请输入手机号..." v-model="ruleForm.phone">
                    <i slot="prefix" class="el-icon-phone"></i>
                </el-input>
            </el-form-item>
            <el-form-item prop="code">
                <el-row :gutter="18">
                    <el-col :span="18">
                        <el-input placeholder="请输入验证码" v-model="ruleForm.code">
                            <i slot="prefix" class="el-icon-tickets"></i>
                        </el-input>
                    </el-col>
                    <el-col :span="6">
                        <el-button @click="sendCode" :disabled="disabled">{{btnText}}</el-button>
                    </el-col>
                </el-row>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" style="width:100%">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "PhoneLogin",
        components: {},
        props: {
            ruleForm: {
                type: Object,
                require: true
            },
            countDown: {
                type: Number,
                default: 60
            }
        },
        data() {
            let checkPhone = (rule, value, callback) => {
                if(!value) {
                    return callback(new Error('手机空'))
                } else {
                    let reg = /^1[3|4|5|7|8][0-9]\d{8}$/;
                    if(reg.test(value)) {
                        callback()
                    } else {
                        return callback(new Error('请输入正确手机号'))
                    }
                }
            };
            return {
                rules: {
                    phone: [
                        {validator: checkPhone, trigger: 'change'}
                    ],
                    code: [
                        {required: true, message: '验证码不能为空', trigger: blur}
                    ]
                },
                disabled: false,
                btnText: '发送验证码',
                time: 0
            }
        },
        methods: {
            sendCode() {

                this.$refs.ruleForm.validateField('phone', callback => {
                    if(callback) {
                        this.$message.error(callback)
                    } else {
                        //1. 时间开始倒数
                        //2. 按钮进入禁用状态
                        //3. 如果倒计时结束，按钮恢复可用状态，按钮文字变成重新发送，把倒计时重置
                        //4， 倒计时的过程中，按钮文字为：多少s后重新发送
                        let timer = setInterval(() => {
                            this.time--;
                            this.btnText = `${this.time}s后重新发送new`;//this.time + 's后重新发送';
                            this.disabled = true;
                            if (this.time === 0) {
                                this.disabled = false;
                                this.btnText = "重新发送";
                                this.time = this.countDown;
                                clearInterval(timer)
                            }
                        }, 1000);
                        //发送验证码
                        this.$emit('sendCode')
                    }
                })
            }
        },
        mounted() {
            this.time = this.countDown
        },
    }
</script>

<style scoped>

</style>
