<template>
  <NuxtLayout name="admin">
    <a-card title="数据库表结构比对">
      <a-row :gutter="[16, 16]">
        <!-- 源表结构 -->
        <a-col :span="12">
          <SchemaSelector
            v-model:selectedColumns="selectedSourceColumns"
            :schema="sourceSchema"
            title="源表结构"
            @change="handleSourceColumnsChange"
          />
        </a-col>
        
        <!-- 目标表结构 -->
        <a-col :span="12">
          <SchemaSelector
            v-model:selectedColumns="selectedTargetColumns"
            :schema="targetSchema"
            title="目标表结构"
            @change="handleTargetColumnsChange"
          />
        </a-col>
      </a-row>

      <!-- 操作按钮 -->
      <div style="margin-top: 16px; text-align: center;">
        <a-button 
          type="primary" 
          :disabled="!canCompare"
          @click="handleCompare"
          :loading="loading"
        >
          开始比对
        </a-button>
      </div>
    </a-card>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import SchemaSelector from '~/components/SchemaSelector.vue'

// 示例数据
const sourceSchema = ref([
  {
    columnName: 'id',
    dataType: 'int',
    nullable: false,
    comment: '主键ID'
  },
  {
    columnName: 'name',
    dataType: 'varchar(255)',
    nullable: true,
    comment: '名称'
  }
])

const targetSchema = ref([
  {
    columnName: 'id',
    dataType: 'int',
    nullable: false,
    comment: '主键ID'
  },
  {
    columnName: 'name',
    dataType: 'varchar(255)',
    nullable: true,
    comment: '名称'
  }
])

const loading = ref(false)
const selectedSourceColumns = ref([])
const selectedTargetColumns = ref([])

// 是否可以进行比对
const canCompare = computed(() => {
  return selectedSourceColumns.value.length > 0 && selectedTargetColumns.value.length > 0
})

// 处理源表列选择变化
const handleSourceColumnsChange = (columns: any[]) => {
  console.log('Source columns selected:', columns)
}

// 处理目标表列选择变化
const handleTargetColumnsChange = (columns: any[]) => {
  console.log('Target columns selected:', columns)
}

// 处理比对
const handleCompare = async () => {
  loading.value = true
  try {
    // TODO: 实现比对逻辑
    await new Promise(resolve => setTimeout(resolve, 1000))
  } finally {
    loading.value = false
  }
}
</script>