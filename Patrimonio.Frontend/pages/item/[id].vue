<script setup lang="ts">
import type { Item } from '~/types/item';

const route = useRoute();
const id = route.params.id;

const { data: item, pending, error } = await useFetch<Item>(`http://localhost:5000/item/${id}`);
</script>

<template>
  <div>
    <div v-if="pending" class="flex items-center justify-center h-64">
      <ULoadingBar />
    </div>

    <div v-else-if="error" class="flex items-center justify-center h-64">
      <UAlert
        title="Erro ao carregar dados"
        description="Não foi possível carregar os detalhes do patrimônio. Por favor, tente novamente."
        color="error"
        variant="soft"
      />
    </div>

    <ItemDetail v-else-if="item" :item="item" />
  </div>
</template> 