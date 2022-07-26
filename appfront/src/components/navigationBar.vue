<template>
  <div id="NavMenu">
    <h5 id="barTitle">侧边导航栏</h5>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router>
      <template v-for="(item, index) in routes" v-if="!item.hidden">
        <el-menu-item v-if="!item.leaf" :index="item.path" :key="item.index">
          <i :class="item.meta.icon"></i>
          <span slot="title">{{ item.meta.title }}</span>
        </el-menu-item>

        <el-submenu v-if="item.leaf && item.children.length>0"  :index="index+''" :key="index">
          <template slot="title">
            <i :class="item.meta.icon"></i>
            <span>{{item.meta.title}}</span>
          </template>
          <el-menu-item v-if="!child.hidden"  v-for="child in item.children" :index="child.path" :key="child.name">
            <i :class="child.meta.icon"></i>
            <span>{{child.meta.title}}</span>
          </el-menu-item>
        </el-submenu>
      </template>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'navigationBar',
  data () {
    return {}
  },
  computed: {
    routes () {
      // console.log(this.$router.options.routes)
      return this.$router.options.routes
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}

</script>

<style scoped>
#barTitle {
  border-bottom: #68af9b 1px solid;
  background-color: #545c64;
  color: white;
  height: 50px;
}

.el-menu {
  width: 100%;
}
</style>
