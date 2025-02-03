<template>
  <NuxtLayout name="admin">
    <a-card title="数据库表结构比对">
      <a-row :gutter="[16, 16]">
        <!-- 源数据库和表选择 -->
        <a-col :span="12">
          <div style="margin-bottom: 16px;">
            <a-form-item label="源数据库">
            </a-form-item>
            <a-select v-model:value="selectedSourceDatabase" placeholder="选择源数据库" style="width: 100%;">
              <a-select-option v-for="db in databases" :key="db" :value="db">{{ db }}</a-select-option>
            </a-select>
          </div>
          <div style="margin-bottom: 16px;">
            <a-form-item label="源表">
            </a-form-item>
            <a-select v-model:value="selectedSourceTable" placeholder="选择源表" style="width: 100%;">
              <a-select-option v-for="table in sourceTables" :key="table" :value="table">{{ table }}</a-select-option>
            </a-select>
          </div>
          <SchemaSelector
            v-model:selectedColumns="selectedSourceColumns"
            :schema="sourceSchema"
            title="源表结构"
            @change="handleSourceColumnsChange"
          />
        </a-col>
        
        <!-- 目标数据库和表选择 -->
        <a-col :span="12">
          <div style="margin-bottom: 16px;">
            <a-form-item label="目标数据库">
            </a-form-item>
            <a-select v-model:value="selectedTargetDatabase" placeholder="选择目标数据库" style="width: 100%;">
              <a-select-option v-for="db in databases" :key="db" :value="db">{{ db }}</a-select-option>
            </a-select>
          </div>
          <div style="margin-bottom: 16px;">
            <a-form-item label="目标表">
            </a-form-item>
            <a-select v-model:value="selectedTargetTable" placeholder="选择目标表" style="width: 100%;">
              <a-select-option v-for="table in targetTables" :key="table" :value="table">{{ table }}</a-select-option>
            </a-select>
          </div>
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
import { ref, computed, watch } from 'vue'
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

const databases = ref(['database1', 'database2']) // 示例数据库列表
const sourceTables = ref(['table1', 'table2']) // 示例源表列表
const targetTables = ref(['table1', 'table2']) // 示例目标表列表

const selectedSourceDatabase = ref('')
const selectedSourceTable = ref('')
const selectedTargetDatabase = ref('')
const selectedTargetTable = ref('')

// 是否可以进行比对
const canCompare = computed(() => {
  return selectedSourceDatabase.value && selectedSourceTable.value && selectedTargetDatabase.value && selectedTargetTable.value && selectedSourceColumns.value.length > 0 && selectedTargetColumns.value.length > 0
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

// 监听数据库选择变化以更新表列表
watch(selectedSourceDatabase, async (newDb) => {
  // TODO: 根据选择的数据库获取表列表
  sourceTables.value = ['table1', 'table2'] // 示例表列表
})

watch(selectedTargetDatabase, async (newDb) => {
  // TODO: 根据选择的数据库获取表列表
  targetTables.value = ['table1', 'table2'] // 示例表列表
})

</script>