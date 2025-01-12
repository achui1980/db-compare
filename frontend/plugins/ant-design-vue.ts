import Antd from 'ant-design-vue'; //全局使用 
import 'ant-design-vue/dist/reset.css';//样式文件引入
export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.use(Antd);  //全局使用 
    // nuxtApp.vueApp.use(Button).use(Layout)//局部功能使用
});