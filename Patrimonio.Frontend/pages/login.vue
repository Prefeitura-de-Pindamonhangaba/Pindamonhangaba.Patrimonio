<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full">
      <div class="bg-white rounded-xl shadow-lg p-8">
        <div>
          <div class="flex justify-center">
            <img src="~/assets/images/logo-pindamonhangaba.svg" alt="Logo" class="h-24 w-auto" />
          </div>
          <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Sistema de Patrimônio
          </h2>
          <p class="mt-2 text-center text-sm text-gray-700">
            Prefeitura Municipal de Pindamonhangaba
          </p>
        </div>
        <form class="mt-8 space-y-6" @submit.prevent="handleLogin">
          <div class="rounded-md shadow-sm -space-y-px">
            <div>
              <label for="email" class="sr-only">Email</label>
              <input
                id="email"
                v-model="email"
                name="email"
                type="email"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 focus:z-10 sm:text-sm"
                placeholder="Email"
              />
            </div>
            <div>
              <label for="password" class="sr-only">Senha</label>
              <input
                id="password"
                v-model="password"
                name="password"
                type="password"
                required
                class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-primary-500 focus:border-primary-500 focus:z-10 sm:text-sm"
                placeholder="Senha"
              />
            </div>
          </div>

          <div>
            <UButton
              type="submit"
              color="primary"
              class="w-full py-3 flex justify-center items-center"
              :loading="isLoading"
            >
              Entrar no Sistema
            </UButton>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  try {
    // Por enquanto, aceita qualquer credencial
    console.log('Login realizado:', { email: email.value, password: password.value })
    
    // Simula um delay de rede
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // Redireciona para a página inicial
    router.push('/')
  } catch (error) {
    console.error('Erro no login:', error)
  } finally {
    isLoading.value = false
  }
}
</script> 