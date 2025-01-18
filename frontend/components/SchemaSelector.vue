<template>
  <div class="schema-selector">
    <a-card :title="title">
      <!-- 搜索栏 -->
      <a-input-search
        v-model:value="searchText"
        placeholder="搜索列名"
        style="margin-bottom: 16px"
        @change="handleSearch"
      />

      <!-- 表格展示 schema -->
      <a-table
        :columns="columns"
        :data-source="filteredColumns"
        :pagination="false"
        size="middle"
        :row-selection="rowSelection"
        :scroll="{ y: 400 }"
        row-key="columnName"
      >
        <!-- 自定义列渲染 -->
        <template #bodyCell="{ column, record }">
          <!-- 数据类型列 -->
          <template v-if="column.key === 'dataType'">
            <a-tag>{{ record.dataType }}</a-tag>
          </template>
          <!-- 是否可空列 -->
          <template v-if="column.key === 'nullable'">
            <a-tag :color="record.nullable ? 'blue' : 'red'">
              {{ record.nullable ? '可空' : '非空' }}
            </a-tag>
          </template>
        </template>
      </a-table>

      <!-- 已选择列展示 -->
      <div class="selected-columns" v-if="selectedColumns.length">
        <a-divider>已选择的列</a-divider>
        <a-space wrap>
          <a-tag
            v-for="col in selectedColumns"
            :key="col.columnName"
            :closable="true"
            @close="deselectColumn(col)"
          >
            {{ col.columnName }}
          </a-tag>
        </a-space>
      </div>
    </a-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// 定义组件属性
interface Props {
  schema: SchemaColumn[]
  title?: string
}

// Schema 列定义
interface SchemaColumn {
  columnName: string
  dataType: string
  nullable: boolean
  comment?: string
}

const props = withDefaults(defineProps<Props>(), {
  title: '表结构'
})

// 定义事件
const emit = defineEmits<{
  (e: 'update:selectedColumns', columns: SchemaColumn[]): void
  (e: 'change', columns: SchemaColumn[]): void
}>()

// 状态定义
const searchText = ref('')
const selectedRowKeys = ref<string[]>([])
const selectedColumns = ref<SchemaColumn[]>([])

// 表格列定义
const columns = [
  {
    title: '列名',
    dataIndex: 'columnName',
    key: 'columnName',
    width: '30%'
  },
  {
    title: '数据类型',
    dataIndex: 'dataType',
    key: 'dataType',
    width: '25%'
  },
  {
    title: '是否可空',
    dataIndex: 'nullable',
    key: 'nullable',
    width: '15%'
  },
  {
    title: '注释',
    dataIndex: 'comment',
    key: 'comment',
    width: '30%'
  }
]

// 表格选择配置
const rowSelection = {
  selectedRowKeys,
  onChange: (selectedKeys: string[], selectedRows: SchemaColumn[]) => {
    selectedRowKeys.value = selectedKeys
    selectedColumns.value = selectedRows
    emit('update:selectedColumns', selectedRows)
    emit('change', selectedRows)
  }
}

// 过滤后的列数据
const filteredColumns = computed(() => {
  if (!searchText.value) return props.schema
  return props.schema.filter(col => 
    col.columnName.toLowerCase().includes(searchText.value.toLowerCase())
  )
})

// 搜索处理
const handleSearch = () => {
  // 实现搜索逻辑
}

// 取消选择列
const deselectColumn = (column: SchemaColumn) => {
  selectedRowKeys.value = selectedRowKeys.value.filter(key => key !== column.columnName)
  selectedColumns.value = selectedColumns.value.filter(col => col.columnName !== column.columnName)
  emit('update:selectedColumns', selectedColumns.value)
  emit('change', selectedColumns.value)
}
</script>

<style scoped>
.schema-selector {
  width: 100%;
}

.selected-columns {
  margin-top: 16px;
  padding: 8px;
  background: #fafafa;
  border-radius: 4px;
}

:deep(.ant-table-tbody > tr > td) {
  padding: 8px 16px;
}
</style>