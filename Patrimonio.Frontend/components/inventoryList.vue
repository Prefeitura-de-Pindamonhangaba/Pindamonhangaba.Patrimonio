<script setup lang="ts">
import type { TableColumn } from '@nuxt/ui';
import type { Item } from '~/types/item';

let {data: dataApi, status } = await useFetch <Item[]>("http://localhost:5000/item");

let data: Item[] | undefined

data = dataApi.value === null ? undefined : dataApi.value

const columns: TableColumn<Item>[] = [
  {accessorKey: 'assetCode', header: 'Patrimônio'},
  {accessorKey: 'description', header: 'Descrição'},
  {accessorKey: 'inventoried', header: 'Inventoriado'},
  {accessorKey: 'physicalLocation', header: 'Local Físico'},
  {accessorKey: 'oldPhysicalLocation', header: 'Local Físico Antigo'},
]

console.log(status)
</script>

<template>
  <UTable :data="data" :columns="columns" :loading="status === 'pending'" class="flex-1" />
</template>
