<template>
  <div class="login-container">
    <a-card title="用户登录" :style="{ width: '400px' }">
      <a-form
        :model="formState"
        name="login"
        :label-col="{ style: { width: '80px' } }"
        @finish="handleFinish"
        @finishFailed="handleFinishFailed"
      >
        <a-form-item
          label="用户名"
          name="username"
          :rules="[{ required: true, message: '请输入用户名!' }]"
        >
          <a-input v-model:value="formState.username">
            <template #prefix>
              <UserOutlined />
            </template>
          </a-input>
        </a-form-item>

        <a-form-item
          label="密码"
          name="password"
           :label-col="{ style: { width: '80px' } }"
          :rules="[{ required: true, message: '请输入密码!' }]"
        >
          <a-input-password v-model:value="formState.password">
            <template #prefix>
              <LockOutlined />
            </template>
          </a-input-password>
        </a-form-item>

        <a-form-item>
          <a-button type="primary" html-type="submit" :style="{ width: '100%' }">
            登录
          </a-button>
        </a-form-item>
      </a-form>
    </a-card>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false
})
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue'
import { reactive } from 'vue'
const router = useRouter()
interface FormState {
  username: string
  password: string
}

const formState = reactive<FormState>({
  username: '',
  password: ''
})

const handleFinish = (values: FormState) => {
  console.log('登录成功:', values)
  router.push('/dashboard')

}

const handleFinishFailed = (errorInfo: any) => {
  console.log('登录失败:', errorInfo)
}
</script>

<style scoped>
.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f0f2f5;
}
</style>