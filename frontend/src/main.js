import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)

Vue.prototype.$hostname = 'http://127.0.0.1:5000'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'

new Vue({
  render: h => h(App),
}).$mount('#app')
