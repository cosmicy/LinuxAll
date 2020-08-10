<template>
    <div>
        <table>
            <tr>
                <td>编号</td>
                <td>图书名称</td>
                <td>作者</td>
            </tr>
            <tr v-for="book in books" :key="book">
                <td>{{book.id}}</td>
                <td>{{book.name}}</td>
                <td>{{book.author}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Book",
        components: {},
        props: {},
        data() {
            return {
                books: [
                    {
                        id: 1,
                        name: 'vue',
                        author: 'zzz'
                    },
                    {
                        id: 2,
                        name: 'java',
                        author: 'xxx'
                    },
                    {
                        id: 3,
                        name: 'springboot',
                        author: 'ccc'
                    }
                ]
            }
        },
        methods: {},
        mounted() {
            axios.get('http://localhost:8181/book/findAll/').then( resp => {
                console.log(resp);
                this.books = resp.data;
            })
        },
    }
</script>

