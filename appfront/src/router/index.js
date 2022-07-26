import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '../components/HelloWorld'
import Login from '../components/Login/Login'
import Register from '../components/Login/Register'
import User from '../components/Login/User'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      hidden: true,
      name: 'index',
      component: HelloWorld
    },
    {
      path: '/helloWorld',
      name: 'HelloWorld',
      component: HelloWorld,
      meta: {
        title: '你好',
        icon: 'el-icon-monitor'
      }
    },
    {
      path: '/user',
      name: 'User',
      leaf: true,
      component: User,
      meta: {
        title: '用户',
        icon: 'el-icon-s-custom'
      },
      children: [
        {
          path: '/register',
          name: 'Register',
          component: Register,
          meta: {
            title: '注册'
          }
        },
        {
          path: '/login',
          name: 'Login',
          component: Login,
          meta: {
            title: '登录'
          }
        }
      ]
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

export default router
