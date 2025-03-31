<template>
  <div class="container mx-auto">
    <div class="flex flex-col items-center justify-center min-h-[calc(100vh-8rem)]">
      <h1 class="text-2xl font-bold mb-8">Leitor de Código de Barras</h1>
      
      <!-- Área do Leitor -->
      <div class="w-full max-w-2xl aspect-video bg-gray-100 dark:bg-gray-800 rounded-lg overflow-hidden mb-8">
        <div v-if="!isScanning" class="w-full h-full flex items-center justify-center">
          <p class="text-gray-500 dark:text-gray-400">Clique em "Iniciar Leitor" para começar</p>
        </div>
        <StreamBarcodeReader
          v-else
          @decode="onDecode"
          @error="onError"
          class="w-full h-full"
        />
      </div>

      <!-- Controles -->
      <div class="flex flex-col sm:flex-row gap-4">
        <UButton
          icon="i-lucide-camera"
          :label="isScanning ? 'Reiniciar Leitor' : 'Iniciar Leitor'"
          color="primary"
          @click="startScanner"
        />
        <UButton
          v-if="isScanning"
          icon="i-lucide-stop-circle"
          label="Parar Leitor"
          color="error"
          @click="stopScanner"
        />
      </div>

      <!-- Resultado -->
      <div class="mt-8 w-full max-w-2xl">
        <h2 class="text-xl font-semibold mb-4">Último Código Lido</h2>
        <div class="bg-white dark:bg-gray-800 p-4 rounded-lg border border-gray-200 dark:border-gray-700">
          <div v-if="lastScannedCode" class="space-y-4">
            <div class="flex items-center justify-between">
              <p class="text-lg font-medium">{{ lastScannedCode }}</p>
              <UButton
                icon="i-lucide-copy"
                color="neutral"
                variant="ghost"
                @click="copyToClipboard(lastScannedCode)"
              />
            </div>
            <div v-if="isLoading" class="flex items-center justify-center py-4">
              <ULoadingIcon />
            </div>
            <div v-else-if="error" class="text-red-500 dark:text-red-400">
              {{ error }}
            </div>
            <div v-else-if="item" class="space-y-2">
              <div class="grid grid-cols-2 gap-2 text-sm">
                <div class="font-medium">Nome:</div>
                <div>{{ item.description }}</div>
                <div class="font-medium">Local:</div>
                <div>{{ item.physicalLocation?.description || 'Não especificado' }}</div>
                <div class="font-medium">Status:</div>
                <div>
                  <UBadge
                    :color="item.status === 'active' ? 'success' : 'error'"
                    :label="item.status === 'active' ? 'Ativo' : 'Inativo'"
                  />
                </div>
              </div>
              <UButton
                label="Ver Detalhes"
                color="primary"
                variant="ghost"
                :to="`/item/${item.id}`"
                class="mt-2"
              />
            </div>
          </div>
          <p v-else class="text-gray-500 dark:text-gray-400">Nenhum código lido ainda</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { StreamBarcodeReader } from 'vue-barcode-reader'
import type { Item } from '~/types/item'

const isScanning = ref(false)
const lastScannedCode = ref<string | null>(null)
const item = ref<Item | null>(null)
const error = ref<string | null>(null)
const isLoading = ref(false)

const startScanner = () => {
  isScanning.value = true
  error.value = null
}

const stopScanner = () => {
  isScanning.value = false
}

const onDecode = async (code: string) => {
  console.log('Código lido:', code) // Log para debug
  lastScannedCode.value = code
  await searchItem(code)
}

const onError = (err: Error) => {
  console.error('Erro na leitura:', err) // Log para debug
  error.value = `Erro ao ler código: ${err.message}`
}

const searchItem = async (code: string) => {
  isLoading.value = true
  error.value = null
  item.value = null

  try {
    const response = await fetch(`http://localhost:5000/api/item?search=${encodeURIComponent(code)}`)
    if (!response.ok) {
      if (response.status === 404) {
        error.value = 'Item não encontrado'
        return
      }
      throw new Error('Erro ao buscar item')
    }
    const data = await response.json()
    if (data && data.length > 0) {
      item.value = data[0]
    } else {
      error.value = 'Item não encontrado'
    }
  } catch (err) {
    error.value = 'Erro ao buscar item no banco de dados'
    console.error('Erro ao buscar item:', err)
  } finally {
    isLoading.value = false
  }
}

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
  } catch (err) {
    console.error('Erro ao copiar para a área de transferência:', err)
  }
}
</script> 