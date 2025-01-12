<template>
  <div class="uploader-container">
    <a-upload-dragger
      v-model:fileList="fileList"
      :action="uploadUrl"
      :accept="acceptTypes"
      :multiple="multiple"
      :beforeUpload="handleBeforeUpload"
      @change="handleChange"
    >
      <p class="ant-upload-drag-icon">
        <InboxOutlined />
      </p>
      <p class="ant-upload-text">点击或拖拽文件到此区域进行上传</p>
      <p class="ant-upload-hint" v-if="acceptTypes">
        支持的文件类型: {{ acceptTypes }}
      </p>
    </a-upload-dragger>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { InboxOutlined } from '@ant-design/icons-vue'
import type { UploadChangeParam, UploadProps } from 'ant-design-vue'

interface Props {
  uploadUrl: string
  acceptTypes?: string
  multiple?: boolean
  maxSize?: number // 单位: MB
}

const props = withDefaults(defineProps<Props>(), {
  multiple: false,
  maxSize: 10,
  acceptTypes: ''
})

const emit = defineEmits<{
  (e: 'success', file: any): void
  (e: 'error', error: any): void
  (e: 'change', fileList: any[]): void
}>()

const fileList = ref<any[]>([])

const handleBeforeUpload = (file: File) => {
  // 检查文件大小
  const isLtMaxSize = file.size / 1024 / 1024 < props.maxSize

  if (!isLtMaxSize) {
    message.error(`文件必须小于 ${props.maxSize}MB!`)
    return false
  }

  return true
}

const handleChange = (info: UploadChangeParam) => {
  fileList.value = info.fileList

  if (info.file.status === 'done') {
    emit('success', info.file)
    message.success(`${info.file.name} 上传成功`)
  } else if (info.file.status === 'error') {
    emit('error', info.file)
    message.error(`${info.file.name} 上传失败`)
  }

  emit('change', fileList.value)
}
</script>

<style scoped>
.uploader-container {
  width: 100%;
}

:deep(.ant-upload-drag) {
  border: 2px dashed #d9d9d9;
}

:deep(.ant-upload-drag:hover) {
  border-color: #1890ff;
}
</style>