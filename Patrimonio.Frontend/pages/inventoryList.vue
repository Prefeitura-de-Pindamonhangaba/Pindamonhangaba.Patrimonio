<script setup lang="ts">
import type { DropdownMenuItem, TableColumn } from '@nuxt/ui';
import type { Item } from '~/types/item';
import { refDebounced } from '@vueuse/core';

const currentPage = ref(1);
const perPage = ref(10);
const searchQuery = ref('');
const totalItems = ref(0);
const totalPages = ref(1);

// Debounce para evitar muitas requisições durante a digitação
const debouncedSearch = refDebounced(searchQuery, 500);

// Observa mudanças na busca e atualiza os dados
watch(debouncedSearch, async () => {
  currentPage.value = 1; // Reset para primeira página ao buscar
  await refresh();
});

const { data: dataApi, pending, error, refresh } = await useAsyncData<{
  items: Item[];
  total: number;
  page: number;
  per_page: number;
  total_pages: number;
}>('items', () => 
  $fetch('http://localhost:5000/item', {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    credentials: 'include',
    mode: 'cors',
    params: {
      page: currentPage.value,
      per_page: perPage.value,
      search: searchQuery.value
    }
  }),
  {
    immediate: true,
    watch: [currentPage, debouncedSearch]
  }
);

const data = computed(() => {
  if (!dataApi.value) return undefined;
  return dataApi.value.items;
});

// Atualiza os totais quando os dados mudam
watch(dataApi, (newData) => {
  if (newData) {
    totalItems.value = newData.total;
    totalPages.value = newData.total_pages;
    currentPage.value = newData.page;
  }
}, { immediate: true });

const handlePageChange = async (page: number) => {
  currentPage.value = page;
};

const columns: TableColumn<Item>[] = [
  {accessorKey: 'assetCode', header: 'Patrimônio'},
  {accessorKey: 'description', header: 'Descrição'},
  {accessorKey: 'inventoried', header: 'Inventariado'},
  {accessorKey: 'physicalLocation.description', header: 'Local Físico'},
  {accessorKey: 'oldPhysicalLocation.description', header: 'Local Físico Antigo'},
  {id: 'action'}
]

const router = useRouter();
const toast = useToast();

const handleRowClick = (row: Item) => {
  router.push(`/item/${row.id}`);
}

const handleRefresh = () => {
  refresh();
}

function getDropdownActions(item: Item): DropdownMenuItem[][] {
  return [
    [
      {
        label: 'Copia Patrimônio',
        icon: 'i-lucide-copy',
        onSelect: () => {
          navigator.clipboard.writeText(item.assetCode.toString())
          toast.add({
            title: 'Patrimônio ID copied to clipboard!',
            color: 'success',
            icon: 'i-lucide-circle-check'
          })
        }
      }
    ],
    [
      {
        label: 'Ver Detalhes',
        icon: 'i-lucide-eye',
        onSelect: () => handleRowClick(item)
      },
      {
        label: 'Delete',
        icon: 'i-lucide-trash',
        color: 'error'
      }
    ]
  ]
}
</script>

<template>
  <div>
    <div v-if="error" class="flex items-center justify-center h-64">
      <div class="text-center space-y-4">
        <UAlert
          title="Erro ao carregar dados"
          description="Não foi possível carregar a lista de patrimônios. Por favor, tente novamente."
          color="error"
          variant="soft"
        />
        <UButton
          icon="i-lucide-refresh-cw"
          color="primary"
          variant="solid"
          @click="handleRefresh"
        >
          Tentar Novamente
        </UButton>
      </div>
    </div>
    <div v-else class="space-y-4">
      <div class="flex items-center justify-between">
        <UInput
          v-model="searchQuery"
          icon="i-lucide-search"
          placeholder="Buscar patrimônios..."
          class="max-w-sm"
          :loading="pending"
        />
      </div>
      <UTable 
        :data="data" 
        :columns="columns" 
        class="flex-1" 
      >
        <template #action-cell="{ row }">
          <UDropdownMenu :items="getDropdownActions(row.original)">
            <UButton
              icon="i-lucide-ellipsis-vertical"
              color="neutral"
              variant="ghost"
              aria-label="Actions"
            />
          </UDropdownMenu>
        </template>
      </UTable>
      <div class="fixed bottom-0 left-0 right-0 border-t border-gray-200 dark:border-gray-700 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm z-10 md:left-[280px]">
        <div class="px-4 py-3">
          <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="text-sm text-gray-500 dark:text-gray-400 text-center sm:text-left">
              Mostrando {{ (currentPage - 1) * perPage + 1 }} a {{ Math.min(currentPage * perPage, totalItems) }} de {{ totalItems }} itens
            </div>
            <div class="flex items-center gap-2 sm:gap-3">
              <UButton
                icon="i-lucide-chevron-left"
                color="primary"
                variant="ghost"
                :disabled="currentPage === 1"
                @click="handlePageChange(currentPage - 1)"
                class="min-w-[36px] h-9 sm:min-w-[40px] sm:h-10"
              />
              <div class="flex items-center gap-1">
                <template v-for="page in totalPages" :key="page">
                  <UButton
                    v-if="page === 1 || page === totalPages || (page >= currentPage - 1 && page <= currentPage + 1)"
                    :color="page === currentPage ? 'primary' : 'neutral'"
                    :variant="page === currentPage ? 'solid' : 'ghost'"
                    @click="handlePageChange(page)"
                    class="min-w-[36px] h-9 sm:min-w-[40px] sm:h-10 flex items-center justify-center text-sm sm:text-base"
                  >
                    {{ page }}
                  </UButton>
                  <span
                    v-else-if="page === currentPage - 2 || page === currentPage + 2"
                    class="px-1 sm:px-2 text-gray-500 dark:text-gray-400 text-sm sm:text-base"
                  >
                    ...
                  </span>
                </template>
              </div>
              <UButton
                icon="i-lucide-chevron-right"
                color="primary"
                variant="ghost"
                :disabled="currentPage === totalPages"
                @click="handlePageChange(currentPage + 1)"
                class="min-w-[36px] h-9 sm:min-w-[40px] sm:h-10"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="h-16"></div>
    </div>
  </div>
</template>

