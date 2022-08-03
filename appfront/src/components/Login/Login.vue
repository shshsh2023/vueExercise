<template>
  <div id="Login">
    <el-form :model="loginForm" :rules="rules" label-width="80px"  ref="loginForm" class="loginForm">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="loginForm.password" ref="password"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="code" id="codeItem">
        <el-input placeholder="点击图片更换验证码" id="codeInput" v-model="loginForm.code" ref="verifyCode"></el-input>
        <el-image :src="codeImageUrl" @click="getVerifyCode" alt="验证码图片" id="codeImage"></el-image>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">登录</el-button>
        <el-button @click="toRegister">注册</el-button>
      </el-form-item>
   </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      codeImageUrl: '',
      loginForm: {
        username: '',
        password: '',
        code: ''
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 5, max: 20, message: '长度在5-20之内', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 5, max: 100, message: '长度在5-100之间', trigger: 'blur'}
        ],
        code: [
          {required: true, message: '请输入验证码', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    submitForm () {
      this.$refs.loginForm.validate((valid) => {
        let username = this.loginForm['username']
        if (valid) {
          axios.post('/lg/login/', this.loginForm)
            .then(function (response) {
              alert(response.data)
              if (response.data === '登录成功') {
                window.sessionStorage.setItem('username', username)
                location.href = '/helloWorld'
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        } else {
          console.log('error submit!')
          return false
        }
      })
    },
    toRegister () {
      this.$router.push('/register')
    },
    getVerifyCode () {
      this.$http({
        url: '/vc/returnImageVerifyCode/',
        method: 'get',
        responseType: 'blob'
      })
        .then((response) => {
          let blob = new Blob([response.data]) // 返回的文件流数据
          // 将他转化为路径
          this.codeImageUrl = window.URL.createObjectURL(blob) // 将转换出来的路径赋值给变量，其实和上一步结合就可以
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.$nextTick(function () {
      this.getVerifyCode()
    })
  }
}
</script>

<style scoped>
.el-form-item {
  width: 45%;
  margin:5px auto;
}
</style>

<style>
#codeItem div:first-child{
  display: inline-block;
  width: 70%;
  float: left;

}
#codeImage {
  display: inline-block;
  float: right;
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
