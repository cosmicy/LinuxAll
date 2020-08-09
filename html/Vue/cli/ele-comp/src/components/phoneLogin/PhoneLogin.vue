<template>
    <div>
        <el-form>
            <el-form-item>
                <el-input placeholder="请输入手机号...">
                    <i slot="prefix" class="el-icon-phone"></i>
                </el-input>
            </el-form-item>
            <el-form-item>
                <el-row :gutter="18">
                    <el-col :span="18">
                        <el-input placeholder="请输入验证码">
                            <i slot="prefix" class="el-icon-tickets"></i>
                        </el-input>
                    </el-col>
                    <el-col :span="6">
                        <el-button>发送验证码</el-button>
                    </el-col>
                </el-row>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" style="width:100%"></el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "PhoneLogin",
        components: {},
        props: {},
        data() {
            return {}
        },
        methods: {},
        mounted() {
        },
    }
</script>

<style scoped>

</style>
