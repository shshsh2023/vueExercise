<template>
  <div id="Register">
    <el-form :model="registerForm" :rules="rules" label-width="80px" ref="registerForm" class="registerForm">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="registerForm.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="registerForm.password" ref="password"></el-input>
      </el-form-item>
      <el-form-item label="重复密码" prop="re_password">
        <el-input type="password" v-model="registerForm.re_password"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input type="email" v-model="registerForm.email" style="width: 64%; display: inline-block;"></el-input>
        <el-button @click="getVerifyCode" style="display: inline-block; width: 34%;">获取验证码</el-button>
      </el-form-item>
      <el-form-item label="验证码" prop="verifyCode">
        <el-input v-model="registerForm.verifyCode"></el-input>
      </el-form-item>
      <el-form-item label="姓" prop="firstName">
        <el-input v-model="registerForm.firstName"></el-input>
      </el-form-item>
      <el-form-item label="名" prop="lastName">
        <el-input v-model="registerForm.lastName"></el-input>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input type="age" v-model.number="registerForm.age"></el-input>
      </el-form-item>
      <el-form-item label="生日" prop="birthday">
        <el-date-picker type="date" v-model="registerForm.birthday" placeholder="选择日期"></el-date-picker>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-radio-group v-model="registerForm.sex" size="small">
          <el-radio-button border label="男"></el-radio-button>
          <el-radio-button border label="女"></el-radio-button>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm()">注册</el-button>
        <el-button @click="resetForm('registerForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Register',
  data () {
    const checkAge = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请输入年龄'))
      } else {
        if (value < 18) {
          callback(new Error('必须年满18岁'))
        } else if (value > 123) {
          callback(new Error('年龄必须小于123'))
        } else {
          callback()
        }
      }
    }
    const checkPdAndRePd = (rule, value, callback) => {
      const password = this.$refs.password.value
      if (value !== password) {
        callback(new Error('两次密码不相同'))
      } else {
        callback()
      }
    }
    return {
      registerForm: {
        username: '',
        password: '',
        re_password: '',
        email: '',
        verifyCode: '',
        firstName: '',
        lastName: '',
        age: '',
        sex: ''
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 5, max: 10, message: '长度在5到10个字符', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 8, max: 128, message: '长度在8到128个字符', trigger: 'blur'}
        ],
        re_password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 8, max: 128, message: '长度在8到128个字符', trigger: 'blur'},
          {validator: checkPdAndRePd, trigger: ['blur', 'change']}
        ],
        email: [
          {required: true, message: '请输入邮箱', trigger: 'blur'},
          {type: 'email', trigger: 'blur'}
        ],
        verifyCode: [
          {required: true, message: '请输入验证码', trigger: 'blur'},
          {min: 6, max: 6, message: '输入六位数字验证码', trigger: 'blur'},
          {pattern: /^[0-9_]+$/, message: '只能由数字组成', trigger: ['blur', 'change']}
        ],
        age: [
          {type: 'number', message: '请输入数值', trigger: 'blur'},
          {required: true, message: '请输入验证码', trigger: 'blur'},
          {validator: checkAge, trigger: 'blur'}
        ],
        sex: [
          {required: true, message: '请选择性别', trigger: 'blur'}
        ],
        birthday: [
          {required: true, message: '请选择生日', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    submitForm () {
      let formData = new FormData()
      for (const key in this.registerForm) {
        if (key === 'birthday') {
          let bir = this.registerForm[key]
          let year = bir.getFullYear()
          let month = bir.getMonth()
          let day = bir.getDay()
          if (month < 10) {
            month = '0' + month
          }
          if (day < 10) {
            day = '0' + day
          }
          let birthday = year + '-' + month + '-' + day
          formData.append(key, birthday)
        } else {
          formData.append(key, this.registerForm[key])
        }
      }
      this.$refs.registerForm.validate((valid) => {
        if (valid) {
          axios.post('/lg/creatNewUser/', formData)
            .then(function (response) {
              if (response.data === '注册成功') {
                alert('注册成功，即将返回登录界面！')
                location.href = '/login'
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
    resetForm (formName) {
      // 下面两种都可以
      this.$refs.registerForm.resetFields()
      // this.$refs[formName].resetFields()
    },
    getVerifyCode () {
      console.log(this.registerForm['email'])
      axios.post('/lg/getVerifyCode/', { 'email': this.registerForm['email'] })
    }
  }
}
</script>
<!--

  如果 this.$refs[formName].validate() 方式不识别。需要使用: this.$refs.formName.validate()
  验证器的每个if都必须匹配else

-->
<style scoped>
.el-form-item {
  width:450px;
  margin-left: auto;
  margin-right: auto;
}
</style>
