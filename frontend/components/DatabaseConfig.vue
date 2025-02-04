<template>
  <div class="database-config">
    <a-row :gutter="[16, 16]">
      <a-col :span="24">
        <a-space>
          <a-button type="primary" @click="showAddDbModal">
            <PlusOutlined /> 添加数据库连接
          </a-button>
        </a-space>
      </a-col>
      <a-col :span="24">
        <a-table :columns="columns" :data-source="connections" row-key="id">
          <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'action'">
              <a-space>
                <a-button 
                  type="primary" 
                  size="small" 
                  @click="handleTestConnection(record)"
                  :loading="testLoading[record.id]"
                >
                  测试连接
                </a-button>
                <a-button type="link" @click="handleEdit(record)">编辑</a-button>
                <a-popconfirm
                  title="确定要删除这个连接吗？"
                  @confirm="handleDelete(record)"
                >
                  <a-button type="link" danger>删除</a-button>
                </a-popconfirm>
              </a-space>
            </template>
            <template v-if="column.key === 'type'">
              <a-tag :color="getDbTypeColor(record.type)">{{ record.type }}</a-tag>
            </template>
          </template>
        </a-table>
      </a-col>
    </a-row>

    <!-- 数据库连接表单弹窗 -->
    <a-modal
      v-model:visible="modalVisible"
      :title="isEdit ? '编辑数据库连接' : '添加数据库连接'"
      @ok="handleModalOk"
      @cancel="handleModalCancel"
    >
      <a-form 
        ref="formRef"
        :model="formState"
        :rules="rules"
        :label-col="{ span: 6 }"
        :wrapper-col="{ span: 16 }"
      >
        <a-form-item label="连接名称" name="name">
          <a-input v-model:value="formState.name" />
        </a-form-item>
        <a-form-item label="数据库类型" name="type">
          <a-select v-model:value="formState.type">
            <a-select-option value="MySQL">MySQL</a-select-option>
            <a-select-option value="PostgreSQL">PostgreSQL</a-select-option>
            <a-select-option value="SQLServer">SQL Server</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="主机地址" name="host">
          <a-input v-model:value="formState.host" />
        </a-form-item>
        <a-form-item label="端口" name="port">
          <a-input-number v-model:value="formState.port" :min="1" :max="65535" />
        </a-form-item>
        <a-form-item label="数据库名" name="database">
          <a-input v-model:value="formState.database" />
        </a-form-item>
        <a-form-item label="用户名" name="username">
          <a-input v-model:value="formState.username" />
        </a-form-item>
        <a-form-item label="密码" name="password">
          <a-input-password v-model:value="formState.password" />
        </a-form-item>
      </a-form>
      <template #footer>
        <a-space>
          <a-button @click="handleModalCancel">取消</a-button>
          <a-button 
            type="primary" 
            @click="handleTestConnectionInModal"
            :loading="modalTestLoading"
          >
            测试连接
          </a-button>
          <a-button type="primary" @click="handleModalOk">确定</a-button>
        </a-space>
      </template>
    </a-modal>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { message } from 'ant-design-vue'
import { PlusOutlined } from '@ant-design/icons-vue'
import type { FormInstance } from 'ant-design-vue'
import {ApiError, apiService, OpenAPI} from '@/client' // 引入request方法和OpenAPIConfig

interface DbConnection {
  id: string
  name: string
  type: string
  host: string
  port: number
  database: string
  username: string
  password: string
}

const columns = [
  { title: '连接名称', dataIndex: 'name', key: 'name' },
  { title: '数据库类型', dataIndex: 'type', key: 'type' },
  { title: '主机地址', dataIndex: 'host', key: 'host' },
  { title: '数据库名', dataIndex: 'database', key: 'database' },
  { title: '操作', key: 'action', width: 200 }
]

const connections = ref<DbConnection[]>([])
const modalVisible = ref(false)
const isEdit = ref(false)
const testLoading = ref<Record<string, boolean>>({})
const formRef = ref<FormInstance>()

const formState = reactive({
  id: '',
  name: '222',
  type: 'MySQL',
  host: 'www.zhangyulu.cn',
  port: 33306,
  database: 'db-compare',
  username: 'root',
  password: 'admin'
})

const rules = {
  name: [{ required: true, message: '请输入连接名称' }],
  type: [{ required: true, message: '请选择数据库类型' }],
  host: [{ required: true, message: '请输入主机地址' }],
  port: [{ required: true, message: '请输入端口号' }],
  database: [{ required: true, message: '请输入数据库名' }],
  username: [{ required: true, message: '请输入用户名' }],
  password: [{ required: true, message: '请输入密码' }]
}

const showAddDbModal = () => {
  isEdit.value = false
  resetForm()
  modalVisible.value = true
}

const handleEdit = (record: DbConnection) => {
  isEdit.value = true
  Object.assign(formState, record)
  modalVisible.value = true
}

const handleDelete = async (record: DbConnection) => {
  try {
    // TODO: 实现删除逻辑
    connections.value = connections.value.filter(item => item.id !== record.id)
    message.success('删除成功')
  } catch (error) {
    message.error('删除失败')
  }
}

const handleTestConnection = async (record: DbConnection) => {
  testLoading.value[record.id] = true
  try {
    // TODO: 实现测试连接逻辑
    await apiService(OpenAPI,{
      method:'POST',
      url:'/api/v1/db_configs/test-connection',
      body:formState})
    message.success('连接成功')
  } catch (error) {
    message.error('连接失败')
  } finally {
    testLoading.value[record.id] = false
  }
}

const handleModalOk = () => {
  formRef.value?.validate().then(async () => {
    try {
      if (isEdit.value) {
        // TODO: 实现更新逻辑
      } else {
        // TODO: 实现新增逻辑
        formState.id = Date.now().toString()
        connections.value.push({ ...formState })
      }
      modalVisible.value = false
      message.success(`${isEdit.value ? '更新' : '添加'}成功`)
    } catch (error) {
      message.error(`${isEdit.value ? '更新' : '添加'}失败`)
    }
  })
}

const handleModalCancel = () => {
  modalVisible.value = false
  resetForm()
}

const resetForm = () => {
  formRef.value?.resetFields()
}

const getDbTypeColor = (type: string) => {
  const colors: Record<string, string> = {
    'MySQL': 'blue',
    'PostgreSQL': 'green',
    'SQLServer': 'purple'
  }
  return colors[type] || 'default'
}

// 添加测试加载状态
const modalTestLoading = ref(false)

// 添加弹窗中的测试连接方法
const handleTestConnectionInModal = async () => {
  let response
  try {
    await formRef.value?.validate()
    modalTestLoading.value = true
    // TODO: 实现实际的测试连接逻辑
    response = await apiService(OpenAPI,{
      method:'POST',
      url:'/api/v1/db_configs/test-connection',
      body:formState
    })
    message.success('连接测试成功')
  } catch (error) {
    console.log("error", response)
    if (error instanceof ApiError) {
      message.error(error.body.msg || '连接测试失败')
    } else {
      message.error('表单验证失败')
    }
  } finally {
    modalTestLoading.value = false
  }
}
</script>

<style scoped>
.database-config {
  width: 100%;
}
</style>