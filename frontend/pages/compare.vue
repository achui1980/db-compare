<template>
  <NuxtLayout name="admin">
    <a-card title="数据表对比">
      <a-row :gutter="[16, 16]">
        <!-- 源表选择 -->
        <a-col :span="12">
          <a-card title="源表">
            <a-form layout="vertical">
              <a-form-item label="选择数据表">
                <a-select
                  v-model:value="sourceTable"
                  placeholder="请选择源表"
                  @change="loadSourceColumns"
                >
                  <a-select-option v-for="table in tables" :key="table" :value="table">
                    {{ table }}
                  </a-select-option>
                </a-select>
              </a-form-item>
            </a-form>
            <!-- 表结构展示 -->
            <a-table
              :columns="structureColumns"
              :data-source="sourceStructure"
              :pagination="false"
              size="small"
            >
              <template #bodyCell="{ column, record }">
                <template v-if="column.key === 'selected'">
                  <a-checkbox v-model:checked="record.selected" />
                </template>
              </template>
            </a-table>
          </a-card>
        </a-col>

        <!-- 目标表选择 -->
        <a-col :span="12">
          <a-card title="目标表">
            <a-form layout="vertical">
              <a-form-item label="选择数据表">
                <a-select
                  v-model:value="targetTable"
                  placeholder="请选择目标表"
                  @change="loadTargetColumns"
                >
                  <a-select-option v-for="table in tables" :key="table" :value="table">
                    {{ table }}
                  </a-select-option>
                </a-select>
              </a-form-item>
            </a-form>
            <!-- 表结构展示 -->
            <a-table
              :columns="structureColumns"
              :data-source="targetStructure"
              :pagination="false"
              size="small"
            />
          </a-card>
        </a-col>

        <!-- 对比按钮 -->
        <a-col :span="24" style="text-align: center;">
          <a-button type="primary" :disabled="!canCompare" @click="compareData">
            开始对比
          </a-button>
        </a-col>

        <!-- 对比结果 -->
        <a-col :span="24" v-if="comparisonResult.length">
          <a-card title="对比结果">
            <a-tabs>
              <a-tab-pane key="different" tab="差异数据">
                <a-table
                  :columns="comparisonColumns"
                  :data-source="comparisonResult"
                  :scroll="{ x: true }"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.diff">
                      <span :class="{ 'diff-highlight': record[column.dataIndex + '_diff'] }">
                        {{ record[column.dataIndex] }}
                      </span>
                    </template>
                  </template>
                </a-table>
              </a-tab-pane>
            </a-tabs>
          </a-card>
        </a-col>
      </a-row>
    </a-card>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// 表结构列定义
const structureColumns = [
  { title: '选择', key: 'selected', width: 60 },
  { title: '字段名', dataIndex: 'column_name', key: 'column_name' },
  { title: '数据类型', dataIndex: 'data_type', key: 'data_type' },
  { title: '是否可空', dataIndex: 'is_nullable', key: 'is_nullable' }
]

const tables = ref<string[]>([])
const sourceTable = ref<string>('')
const targetTable = ref<string>('')
const sourceStructure = ref<any[]>([])
const targetStructure = ref<any[]>([])
const comparisonResult = ref<any[]>([])

// 是否可以进行对比
const canCompare = computed(() => {
  return sourceTable.value && targetTable.value && 
         sourceStructure.value.some(col => col.selected)
})

// 加载表结构
const loadSourceColumns = async () => {
  // 调用后端API获取表结构
  sourceStructure.value = [] // 从API获取数据
}

const loadTargetColumns = async () => {
  // 调用后端API获取表结构
  targetStructure.value = [] // 从API获取数据
}

// 进行数据对比
const compareData = async () => {
  // 调用后端API进行数据对比
  comparisonResult.value = [] // 从API获取对比结果
}
</script>

<style scoped>
.diff-highlight {
  background-color: #ffd6d6;
}
</style>