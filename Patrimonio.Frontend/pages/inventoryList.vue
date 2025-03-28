<script setup lang="ts">
import type { DropdownMenuItem, TableColumn } from '@nuxt/ui';
import type { Item } from '~/types/item';

const { data: dataApi, pending, error } = await useFetch<Item[]>("http://localhost:5000/item");

const data = computed(() => {
  return dataApi.value === null ? undefined : dataApi.value;
});

const columns: TableColumn<Item>[] = [
  {accessorKey: 'assetCode', header: 'Patrimônio'},
  {accessorKey: 'description', header: 'Descrição'},
  {accessorKey: 'inventoried', header: 'Inventariado'},
  {accessorKey: 'physicalLocation.descricao', header: 'Local Físico'},
  {accessorKey: 'oldPhysicalLocation.descricao', header: 'Local Físico Antigo'},
  {id: 'action'}
]

const router = useRouter();
const toast = useToast();

const handleRowClick = (row: Item) => {
  router.push(`/item/${row.id}`);
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
    <div v-if="pending" class="flex items-center justify-center h-64">
      <ULoadingBar />
    </div>
    <div v-else-if="error" class="flex items-center justify-center h-64">
      <UAlert
        title="Erro ao carregar dados"
        description="Não foi possível carregar a lista de patrimônios. Por favor, tente novamente."
        color="error"
        variant="soft"
      />
    </div>
    <UTable 
      v-else
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
  </div>
</template>

