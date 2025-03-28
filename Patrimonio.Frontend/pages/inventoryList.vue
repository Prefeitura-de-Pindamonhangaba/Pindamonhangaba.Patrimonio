<script setup lang="ts">
import type { TableColumn } from '@nuxt/ui';
import type { Item } from '~/types/item';

let {data: dataApi, status, pending } = await useFetch <Item[]>("http://localhost:5000/item");

let data: Item[] | undefined

data = dataApi.value === null ? undefined : dataApi.value

const columns: TableColumn<Item>[] = [
  {accessorKey: 'assetCode', header: 'Patrimônio'},
  {accessorKey: 'description', header: 'Descrição'},
  {accessorKey: 'inventoried', header: 'Inventariado'},
  {accessorKey: 'physicalLocation.descricao', header: 'Local Físico'},
  {accessorKey: 'oldPhysicalLocation.descricao', header: 'Local Físico Antigo'},
]

const router = useRouter();

const handleSelectionChange = (selection: Item[]) => {
  if (selection.length > 0) {
    router.push(`/item/${selection[0].id}`);
  }
}
</script>

<template>
  <UTable 
    :data="data" 
    :columns="columns" 
    :loading="pending" 
    class="flex-1" 
    selectable
    @update:selected="handleSelectionChange"
  />
</template>
