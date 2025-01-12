<template>
  <NuxtLayout name="admin">
    <a-card title="文件对比">
      <a-row :gutter="[16, 16]">
        <a-col :span="12">
          <a-card title="目标文件">
            <FileUploader
              :uploadUrl="uploadUrl"
              acceptTypes=".xlsx,.csv"
              @success="handleTargetSuccess"
              @error="handleUploadError"
            />
          </a-card>
        </a-col>
        <a-col :span="12">
          <a-card title="对比文件">
            <FileUploader
              :uploadUrl="uploadUrl"
              acceptTypes=".xlsx,.csv"
              @success="handleCompareSuccess"
              @error="handleUploadError"
            />
          </a-card>
        </a-col>
      </a-row>
      <div style="margin-top: 16px; text-align: center;">
        <a-button 
          type="primary" 
          :disabled="!canSubmit"
          @click="handleCompare"
          :loading="loading"
        >
          开始对比
        </a-button>
      </div>
    </a-card>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { message } from 'ant-design-vue'

const uploadUrl = '/api/upload'
const loading = ref(false)
const targetFile = ref(null)
const compareFile = ref(null)

const canSubmit = computed(() => {
  return targetFile.value && compareFile.value
})

const handleTargetSuccess = (file: any) => {
  targetFile.value = file.response
}

const handleCompareSuccess = (file: any) => {
  compareFile.value = file.response
}

const handleUploadError = (error: any) => {
  message.error('文件上传失败')
}

const handleCompare = async () => {
  if (!canSubmit.value) return
  
  loading.value = true
  try {
    const res = await fetch('/api/compare', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        targetFile: targetFile.value,
        compareFile: compareFile.value
      })
    })
    const data = await res.json()
    message.success('对比完成')
    // 处理对比结果...
  } catch (error) {
    message.error('对比失败')
  } finally {
    loading.value = false
  }
}
</script>