<template>
  <UApp>
    <div class="flex flex-col md:flex-row h-screen">
      <aside class="w-full md:w-64 bg-gray-200 text-black p-4">
      <div class="mb-8">
        <img src="~/assets/images/logo-pindamonhangaba.svg" alt="Logo da Prefeitura" class="w-48" />
      </div>
      <nav>
        <UButton label="Início" to="/" class="mb-2 w-full" />
        <UButton label="Lista de Patrimônios" to="/inventorylist" class="mb-2 w-full" />
        <UButton label="Contato" to="/contato" class="w-full" />
      </nav>
    </aside>
    <main class="flex-1 p-8">
      <NuxtPage />
    </main>
    </div>
  </UApp>
</template>
