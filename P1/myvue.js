// https://www.8host.com/blog/otobrazhenie-dannyx-iz-api-s-pomoshhyu-vue-js-i-axios/
const url_all = "http://127.0.0.1:8000/api/user/0";
const url_one = "http://127.0.0.1:8000/api/user/";
const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        usr: []
    },

    mounted() {
        axios.get(url_all).then(response => {
            this.results = response.data;
        })
    },
    methods: {


        show_user(id) {
            axios.get(url_one + id).then(response => {
                this.usr = response.data;
                alert('Пользователь: ' + this.usr.name)
            })


        },
        addComment() {
            this.comments.push('Новый комментарий')
        },


        changeWholeArticle() {
            this.article = {text: 'Vue 3 крутой'}
        },
        clearComments() {
            this.comments = []
        }


    }
});