// https://www.8host.com/blog/otobrazhenie-dannyx-iz-api-s-pomoshhyu-vue-js-i-axios/
const url = "http://127.0.0.1:8000/api/user/1";
const vm = new Vue({
el: '#app',
data: {
results: []

},

mounted() {

axios.get(url).then(response => {

this.results = response.data;
//console.log(response.data);

})
}
});