<template>
    <div class="pages-content">
        <el-backtop target=".pages-content"></el-backtop>
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "BackTop"
    }
</script>

<style scoped>
    .pages-content {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        overflow-x: hidden;
    }
</style>
