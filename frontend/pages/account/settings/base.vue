<template>
  <NuxtLayout name="admin">
    <a-card :bordered="false">
      <a-row>
        <a-col :span="6">
          <a-menu
            mode="inline"
            v-model:selectedKeys="selectedKeys"
            style="border-right: 1px solid #f0f0f0"
          >
            <a-menu-item key="base">
              <UserOutlined />
              基本设置
            </a-menu-item>
            <a-menu-item key="security">
              <LockOutlined />
              安全设置
            </a-menu-item>
            <a-menu-item key="binding">
              <LinkOutlined />
              账号绑定
            </a-menu-item>
          </a-menu>
        </a-col>
        <a-col :span="18" style="padding-left: 24px">
          <div v-if="selectedKeys[0] === 'base'">
            <a-form layout="vertical">
              <a-row>
                <a-col :span="10">
                  <a-form-item label="邮箱">
                    <a-input v-model:value="userInfo.email" />
                  </a-form-item>
                  <a-form-item label="昵称">
                    <a-input v-model:value="userInfo.nickname" />
                  </a-form-item>
                  <a-form-item label="个人简介">
                    <a-textarea v-model:value="userInfo.profile" :rows="4" />
                  </a-form-item>
                  <a-form-item label="国家/地区">
                    <a-select v-model:value="userInfo.country">
                      <a-select-option value="china">中国</a-select-option>
                      <a-select-option value="usa">美国</a-select-option>
                    </a-select>
                  </a-form-item>
                  <a-form-item label="所在省市">
                    <a-input v-model:value="userInfo.address" />
                  </a-form-item>
                  <a-form-item>
                    <a-button type="primary">更新基本信息</a-button>
                  </a-form-item>
                </a-col>
                <a-col :span="14" style="padding-left: 48px">
                  <a-form-item label="头像">
                    <div class="avatar-wrapper">
                      <a-upload
                        v-model:file-list="fileList"
                        name="avatar"
                        list-type="picture-card"
                        class="avatar-uploader"
                        :show-upload-list="false"
                        action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                        @change="handleChange"
                      >
                        <img v-if="userInfo.avatar" :src="userInfo.avatar" alt="avatar" />
                        <div v-else>
                          <PlusOutlined />
                          <div class="ant-upload-text">上传</div>
                        </div>
                      </a-upload>
                    </div>
                  </a-form-item>
                </a-col>
              </a-row>
            </a-form>
          </div>
        </a-col>
      </a-row>
    </a-card>
  </NuxtLayout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { UserOutlined, LockOutlined, LinkOutlined, PlusOutlined } from '@ant-design/icons-vue'

const selectedKeys = ref<string[]>(['base'])

const userInfo = ref({
  email: 'ant-design-vue@example.com',
  nickname: 'Serati Ma',
  profile: '海纳百川，有容乃大',
  country: 'china',
  address: '浙江省杭州市',
  avatar: 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png'
})

const fileList = ref([])

const handleChange = (info: any) => {
  if (info.file.status === 'done') {
    userInfo.value.avatar = info.file.response.url
  }
}

definePageMeta({
  layout: false
})
</script>

<style scoped>
.avatar-wrapper {
  text-align: center;
}

.avatar-uploader {
  :deep(.ant-upload) {
    width: 144px;
    height: 144px;
  }
}

.ant-upload-text {
  margin-top: 8px;
  color: #666;
}

:deep(.ant-upload-select-picture-card) img {
  width: 100%;
}
</style>