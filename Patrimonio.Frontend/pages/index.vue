<template>
  <div>
    <main class="flex-1 p-8">
      <div v-if="route.path === '/'" class="space-y-8">
        <div class="bg-gray-800/50 p-8 rounded-lg border border-gray-700">
          <h1 class="text-3xl font-bold mb-4 text-white">
            Sistema de Patrimônio
          </h1>
          <p class="text-xl text-gray-300">
            Prefeitura de Pindamonhangaba
          </p>
        </div>

        </div>
    </main>
  </div>
</template>

<script setup lang="ts">
const route = useRoute();
</script>