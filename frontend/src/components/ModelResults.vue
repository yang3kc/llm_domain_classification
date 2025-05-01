<script setup>
import { ref, onMounted } from 'vue'

const results = ref([])

onMounted(async () => {
  try {
    const response = await fetch('/data/results.json')
    const text = await response.text()
    // Split by newlines and parse each line as JSON
    results.value = text.trim().split('\n').map(line => JSON.parse(line))
  } catch (error) {
    console.error('Error loading results:', error)
  }
})

// Format number to 3 decimal places
const formatNumber = (num) => Number(num).toFixed(3)
</script>

<template>
  <div class="overflow-x-auto">
    <table class="table w-full">
      <thead>
        <tr class="bg-base-200">
          <th>Model</th>
          <th>N</th>
          <th>ρ (Rho)</th>
          <th>p-value</th>
          <th>Significance</th>
          <th>Left/Right</th>
          <th>t-value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="result in results" :key="result.model" class="hover">
          <td class="font-mono text-sm">{{ result.model }}</td>
          <td class="text-right">{{ result.n }}</td>
          <td class="text-right">{{ formatNumber(result.rho) }}</td>
          <td class="text-right">{{ result.rho_p === 0 ? '< 0.001' : formatNumber(result.rho_p) }}</td>
          <td class="text-center">{{ result.rho_stars }}</td>
          <td class="text-right">{{ result.left_n }}/{{ result.right_n }}</td>
          <td class="text-right">{{ formatNumber(result.t) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.table {
  border-collapse: collapse;
  width: 100%;
}

.table th,
.table td {
  padding: 0.75rem;
  border-bottom: 1px solid #e2e8f0;
}

.table th {
  font-weight: 600;
  text-align: left;
}

.hover:hover {
  background-color: #f8fafc;
}
</style>