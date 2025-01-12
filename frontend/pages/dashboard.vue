<template>
  <NuxtLayout name="admin">
    <div class="workplace">
      <!-- 页面头部 -->
      <div class="page-header">
        <a-row :gutter="24">
          <a-col :span="16">
            <div class="avatar-content">
              <a-avatar size="large" src="https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png" />
              <div class="content">
                <div class="title">早安, Admin, 开始您一天的工作吧!</div>
                <div class="welcome">今日晴，20℃ - 32℃！</div>
              </div>
            </div>
          </a-col>
          <a-col :span="8">
            <div class="extra-content">
              <div class="stat-item">
                <a-statistic title="项目数" :value="56" />
              </div>
              <div class="stat-item">
                <a-statistic title="团队内排名" :value="8" suffix="/ 24" />
              </div>
              <div class="stat-item">
                <a-statistic title="项目访问" :value="2223" />
              </div>
            </div>
          </a-col>
        </a-row>
      </div>

      <!-- 主体内容 -->
      <a-row :gutter="24">
        <a-col :span="16">
          <!-- 进行中的项目 -->
          <a-card
            style="margin-bottom: 24px"
            :bordered="false"
            title="进行中的项目"
          >
            <a-card-grid v-for="item in projects" :key="item.id" style="width: 33.33%">
              <a-card :bordered="false">
                <a-card-meta>
                  <template #title>
                    <div class="card-title">
                      <a-avatar :size="small" :src="item.avatar" />
                      <a>{{ item.title }}</a>
                    </div>
                  </template>
                  <template #description>{{ item.description }}</template>
                </a-card-meta>
                <div class="project-item">
                  <span class="datetime">{{ item.updatedAt }}</span>
                </div>
              </a-card>
            </a-card-grid>
          </a-card>

          <!-- 动态 -->
          <a-card
            :bordered="false"
            title="动态"
          >
            <a-list :loading="loading" :data-source="activities">
              <template #renderItem="{ item }">
                <a-list-item>
                  <a-list-item-meta>
                    <template #title>
                      <span>{{ item.user }} 在 {{ item.project }}</span>
                    </template>
                    <template #description>
                      <span>{{ item.time }}</span>
                    </template>
                  </a-list-item-meta>
                </a-list-item>
              </template>
            </a-list>
          </a-card>
        </a-col>

        <a-col :span="8">
          <!-- 快速开始 / 便捷导航 -->
          <a-card style="margin-bottom: 24px" :bordered="false" title="快速开始 / 便捷导航">
            <div class="item-group">
              <a v-for="item in links" :key="item.id">{{ item.title }}</a>
            </div>
          </a-card>

          <!-- 团队 -->
          <a-card :bordered="false" title="团队">
            <div class="members">
              <div v-for="item in teams" :key="item.id" class="member">
                <a-avatar :src="item.avatar" size="small" />
                <span class="member-name">{{ item.name }}</span>
              </div>
            </div>
          </a-card>
        </a-col>
      </a-row>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
const projects = ref([
  {
    id: 1,
    title: 'Alipay',
    avatar: 'https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png',
    description: '那是一种内在的东西，他们到达不了，也无法触及的',
    updatedAt: '2小时前'
  },
  // ... 更多项目数据
])

const activities = ref([
  {
    id: 1,
    user: '曲丽丽',
    project: '高逼格设计天团',
    time: '2小时前'
  },
  // ... 更多动态数据
])

const links = ref([
  { id: 1, title: '操作一' },
  { id: 2, title: '操作二' },
  // ... 更多链接
])

const teams = ref([
  {
    id: 1,
    name: '科学搬砖组',
    avatar: 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png'
  },
  // ... 更多团队数据
])
</script>

<style scoped>
.workplace {
  padding: 24px;
}

.page-header {
  background: #fff;
  padding: 24px;
  margin-bottom: 24px;
}

.avatar-content {
  display: flex;
  align-items: center;
}

.content {
  margin-left: 24px;
}

.title {
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 12px;
}

.extra-content {
  display: flex;
  justify-content: space-between;
}

.card-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.project-item {
  margin-top: 8px;
}

.datetime {
  color: rgba(0, 0, 0, 0.45);
}

.members {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.member {
  display: flex;
  align-items: center;
  gap: 8px;
}

.item-group {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
}
</style>