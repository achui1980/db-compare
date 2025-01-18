<template>
  <NuxtLayout name="admin">
    <a-card :bordered="false">
      <a-tabs v-model:activeKey="activeKey">
        <!-- 数据库连接设置 -->
        <a-tab-pane key="database" tab="数据库配置">
          <DatabaseConfig />
        </a-tab-pane>

        <!-- 常规设置 -->
        <a-tab-pane key="general" tab="常规设置">
          <a-form :model="generalForm" :label-col="{ span: 6 }" :wrapper-col="{ span: 14 }">
            <a-form-item label="主题">
              <a-select v-model:value="generalForm.theme">
                <a-select-option value="light">浅色</a-select-option>
                <a-select-option value="dark">深色</a-select-option>
              </a-select>
            </a-form-item>
            <a-form-item label="语言">
              <a-select v-model:value="generalForm.language">
                <a-select-option value="zh-CN">中文</a-select-option>
                <a-select-option value="en-US">English</a-select-option>
              </a-select>
            </a-form-item>
          </a-form>
        </a-tab-pane>

        <!-- 其他设置标签页 -->
        <a-tab-pane key="other" tab="其他设置">
          <!-- 其他设置内容 -->
        </a-tab-pane>
      </a-tabs>
    </a-card>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { message } from 'ant-design-vue'

// 当前激活的标签页
const activeKey = ref('database')

// 常规设置表单
const generalForm = reactive({
  theme: 'light',
  language: 'zh-CN',
})

// 数据库连接弹窗相关
const dbModalVisible = ref(false)
const dbModalTitle = ref('添加数据库连接')
const dbModalForm = reactive({
  name: '',
  type: 'mysql',
  host: '',
  port: 3306,
  database: '',
  username: '',
  password: '',
})

// 显示添加数据库弹窗
const showAddDbModal = () => {
  dbModalTitle.value = '添加数据库连接'
  dbModalVisible.value = true
}

// 测试数据库连接
const handleTestConnection = async (record: any) => {
  try {
    // TODO: 实现测试连接逻辑
    message.success('连接成功')
  } catch (error) {
    message.error('连接失败')
  }
}

// 编辑数据库连接
const handleEditDb = (record: any) => {
  dbModalTitle.value = '编辑数据库连接'
  Object.assign(dbModalForm, record)
  dbModalVisible.value = true
}

// 删除数据库连接
const handleDeleteDb = async (record: any) => {
  try {
    // TODO: 实现删除逻辑
    message.success('删除成功')
  } catch (error) {
    message.error('删除失败')
  }
}

// 处理弹窗确认
const handleDbModalOk = async () => {
  try {
    // TODO: 实现保存逻辑
    dbModalVisible.value = false
    message.success('保存成功')
  } catch (error) {
    message.error('保存失败')
  }
}

// 处理弹窗取消
const handleDbModalCancel = () => {
  dbModalVisible.value = false
}
</script>

<style scoped>
.ant-form {
  max-width: 800px;
  margin: 0 auto;
}
</style>