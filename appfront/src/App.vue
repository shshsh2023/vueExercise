<template>
  <div id="app">
    <el-container>
      <el-aside>
        <navigationBar></navigationBar>
      </el-aside>
      <el-container id="mainContent">
        <el-header>学习永无止境</el-header>
        <el-main>
          <!--        主要内容-->
          <router-view></router-view>
        </el-main>
        <el-footer>学习永无止境</el-footer>
      </el-container>
    </el-container>
    <!--    <img src="./assets/logo.png" alt="logo">-->
    <!--    <router-view/>-->
  </div>
</template>

<script>
import navigationBar from './components/navigationBar'

export default {
  name: 'App',
  components: {
    // 标签和vue组件同名
    navigationBar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
  height: 100%;
}

.el-aside::-webkit-scrollbar {
  display: none;
}

.el-aside {
  position: fixed;
  height: 100%;
  background-color: #545c64;
}

.el-header{
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-container {
  height: 100%;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  height: 540px;
  /*height: 100%;*/
}

.el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

#mainContent {
  margin-left: 300px;
  height: 100%;
}
</style>
