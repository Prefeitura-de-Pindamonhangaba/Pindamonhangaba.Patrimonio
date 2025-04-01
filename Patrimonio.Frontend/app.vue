<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isCollapsed = ref(true)
const isLoginPage = computed(() => route.path === '/login')

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
}
</script>

<template>
  <UApp>
    <template v-if="!isLoginPage">
      <!-- Header fixo (apenas para mobile) -->
      <div class="md:hidden fixed top-0 left-0 right-0 bg-white flex items-center justify-between px-4 z-50 border-b">
        <div class="flex items-center">
          <img src="~/assets/images/logo-pindamonhangaba.svg" alt="Logo" class="h-20 w-auto" />
        </div>
        <UButton
          :icon="isCollapsed ? 'i-lucide-menu' : 'i-lucide-x'"
          color="primary"
          variant="ghost"
          @click="toggleSidebar"
          class="!p-2"
        />
      </div>

      <!-- Overlay (apenas para mobile) -->
      <div
        v-if="!isCollapsed"
        class="md:hidden fixed inset-0 bg-black bg-opacity-50 z-40"
        @click="toggleSidebar"
      ></div>

      <div class="flex flex-col md:flex-row h-screen">
        <!-- Menu Lateral (desktop) -->
        <aside class="hidden md:block w-64 bg-gray-200 text-black p-4">
          <div class="mb-8">
            <img src="~/assets/images/logo-pindamonhangaba.svg" alt="Logo da Prefeitura" class="w-48" />
          </div>
          <nav>
            <UButton label="Início" to="/" class="mb-2 w-full" />
            <UButton label="Lista de Patrimônios" to="/inventorylist" class="mb-2 w-full" />
            <UButton label="Leitor de Código" to="/barcodeReader" class="mb-2 w-full" />
          </nav>
        </aside>

        <!-- Menu Mobile -->
        <div
          class="md:hidden fixed top-[5rem] left-0 h-[calc(100vh-5rem)] bg-white text-gray-900 transition-all duration-300 z-50 w-72 border-r"
          :class="[
            isCollapsed ? '-translate-x-full' : 'translate-x-0'
          ]"
        >
          <nav class="p-4">
            <UButton label="Início" to="/" class="mb-2 w-full" @click="toggleSidebar" />
            <UButton label="Lista de Patrimônios" to="/inventorylist" class="mb-2 w-full" @click="toggleSidebar" />
            <UButton label="Leitor de Código" to="/barcodeReader" class="mb-2 w-full" @click="toggleSidebar" />
          </nav>
        </div>

        <!-- Conteúdo Principal -->
        <main class="flex-1 p-8 pt-[5rem] md:pt-8">
          <NuxtPage />
        </main>
      </div>
    </template>
    <template v-else>
      <NuxtPage />
    </template>
  </UApp>
</template>
