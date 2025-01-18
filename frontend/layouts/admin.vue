<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
      <div class="logo" />
      <a-menu
        v-model:selectedKeys="selectedKeys"
        theme="dark"
        mode="inline"
      >
        <a-menu-item key="/dashboard" @click="handleMenuClick('/dashboard')">
          <DashboardOutlined />
          <span>仪表盘</span>
        </a-menu-item>
        <a-menu-item key="/account/settings/base" @click="handleMenuClick('/account/settings/base')">
          <UserOutlined />
          <span>用户管理</span>
        </a-menu-item>
        <a-menu-item key="/upload" @click="router.push('/upload')">
          <UploadOutlined />
          <span>文件上传</span>
        </a-menu-item>
        <a-menu-item key="/compare" @click="router.push('/compare')">
          <SyncOutlined />
          <span>数据比对</span>
        </a-menu-item>
        <a-menu-item key="/settings" @click="router.push('/settings')">
          <SettingOutlined />
          <span>系统设置</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <a-row justify="end" :style="{ paddingRight: '24px' }">
          <a-dropdown>
            <a class="ant-dropdown-link" @click.prevent>
              <UserOutlined /> Admin
            </a>
            <template #overlay>
              <a-menu>
                <a-menu-item key="0">
                  <a href="javascript:;">个人信息</a>
                </a-menu-item>
                <a-menu-item key="1">
                  <a href="javascript:;">退出登录</a>
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </a-row>
      </a-layout-header>
      <a-layout-content style="margin: 24px 16px">
        <slot />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import { ref,watch } from 'vue'
import { UserOutlined, DashboardOutlined, UploadOutlined, SyncOutlined,SettingOutlined} from '@ant-design/icons-vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
// 监听路由变化
watch(() => route.path, (newPath) => {
  selectedKeys.value = [newPath]
})

const collapsed = ref<boolean>(false)
const selectedKeys = ref<string[]>([route.path])

// 菜单点击处理
const handleMenuClick = (path: string) => {
  router.push(path)
}
</script>

<style scoped>
.logo {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.3);
}
</style>