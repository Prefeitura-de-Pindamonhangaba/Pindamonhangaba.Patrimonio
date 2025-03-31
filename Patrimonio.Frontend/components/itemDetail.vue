<script setup lang="ts">
import type { Item } from '~/types/item';

const props = defineProps<{
  item: Item;
}>();

const router = useRouter();

const handleBack = () => {
  router.push('/');
}
</script>

<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <h1 class="text-2xl font-bold text-white">Detalhes do Patrimônio</h1>
      <UButton
        icon="i-heroicons-arrow-left"
        variant="ghost"
        @click="handleBack"
      >
        Voltar
      </UButton>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <UCard>
        <template #header>
          <h2 class="text-xl font-semibold text-white">Informações Básicas</h2>
        </template>

        <div class="space-y-4">
          <div>
            <div class="text-sm text-gray-400">Código do Patrimônio</div>
            <div class="text-white">{{ item.assetCode }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Descrição</div>
            <div class="text-white">{{ item.description }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Referência</div>
            <div class="text-white">{{ item.reference }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Status de Inventário</div>
            <UBadge
              :color="item.inventoried ? 'success' : 'warning'"
              :label="item.inventoried ? 'Inventariado' : 'Não Inventariado'"
            />
          </div>
          <div>
            <div class="text-sm text-gray-400">Status</div>
            <div class="text-white">{{ item.status }}</div>
          </div>
        </div>
      </UCard>

      <UCard>
        <template #header>
          <h2 class="text-xl font-semibold text-white">Informações de Aquisição</h2>
        </template>

        <div class="space-y-4">
          <div>
            <div class="text-sm text-gray-400">Data de Aquisição</div>
            <div class="text-white">{{ item.acquisitionDate ? new Date(item.acquisitionDate).toLocaleDateString() : '-' }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Método de Aquisição</div>
            <div class="text-white">{{ item.acquisitionMethod }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Fornecedor</div>
            <div class="text-white">{{ item.supplier }}</div>
          </div>
        </div>
      </UCard>

      <UCard>
        <template #header>
          <h2 class="text-xl font-semibold text-white">Localização</h2>
        </template>

        <div class="space-y-4">
          <div>
            <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Local Físico</div>
            <div class="mt-1">{{ item.physicalLocation?.description }}</div>
          </div>
          <div>
            <div class="text-sm font-medium text-gray-500 dark:text-gray-400">Local Físico Antigo</div>
            <div class="mt-1">{{ item.oldPhysicalLocation?.description || '-' }}</div>
          </div>
        </div>
      </UCard>

      <UCard>
        <template #header>
          <h2 class="text-xl font-semibold text-white">Informações Adicionais</h2>
        </template>

        <div class="space-y-4">
          <div>
            <div class="text-sm text-gray-400">Data de Criação</div>
            <div class="text-white">{{ new Date(item.createdAt).toLocaleDateString() }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Última Atualização</div>
            <div class="text-white">{{ new Date(item.updatedAt).toLocaleDateString() }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Observações</div>
            <div class="text-white">{{ item.observation || 'Nenhuma observação' }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">URL da Imagem</div>
            <div class="text-white">{{ item.imageUrl || 'Nenhuma imagem' }}</div>
          </div>
          <div>
            <div class="text-sm text-gray-400">Item Alterado</div>
            <UBadge
              :color="item.itemChanged ? 'warning' : 'success'"
              :label="item.itemChanged ? 'Sim' : 'Não'"
            />
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template> 