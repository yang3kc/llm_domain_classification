<script setup>
import { ref, onMounted, computed } from 'vue'

const totalNumberOfDomains = 5653
const results = ref([])
const correlationResults = computed(() => {
  return results.value
    .map(result => ({
      model: result.model,
      n: result.n,
      rho: result.rho,
      rho_p: result.rho_p
    }))
    .sort((a, b) => b.rho - a.rho) // Sort by rho in descending order
})

const biasResults = computed(() => {
  return results.value
    .map(result => ({
      model: result.model,
      left_n: result.left_n,
      right_n: result.right_n,
      t: result.t,
      t_p: result.t_p,
    }))
    .sort((a, b) => a.t - b.t) // Sort by t in ascending order
})

onMounted(async () => {
  try {
    const response = await fetch(`${import.meta.env.BASE_URL}data/results.json`)
    const text = await response.text()
    // Split by newlines and parse each line as JSON
    results.value = text.trim().split('\n').map(line => JSON.parse(line))
  } catch (error) {
    console.error('Error loading results:', error)
  }
})

// Format number to 3 decimal places
const formatNumber = (num) => Number(num).toFixed(3)
const formatPercentage = (num) => (num / totalNumberOfDomains * 100).toFixed(1)

// Convert p-value to significance stars
const pValueToStars = (pValue) => {
  if (pValue < 0.001) return '***'
  if (pValue < 0.01) return '**'
  if (pValue < 0.05) return '*'
  return 'NS' // Not significant
}

// Format p-value with stars
const formatPValue = (pValue) => {
  const stars = pValueToStars(pValue)
  return stars
}
</script>

<template>
  <div class="space-y-8">
    <!-- Correlation Results Table -->
    <div class="overflow-x-auto">
      <h2 class="text-xl font-bold mb-4">Correlation Results (Sorted by ρ)</h2>
      <table class="table w-full">
        <thead>
          <tr class="bg-base-200">
            <th>Model</th>
            <th class="text-right">N (%)</th>
            <th class="text-right">Spearman's ρ</th>
            <th class="text-right">p-value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in correlationResults" :key="result.model" class="hover">
            <td class="font-mono text-sm">{{ result.model }}</td>
            <td class="text-right">{{ result.n }}({{ formatPercentage(result.n) }}%)</td>
            <td class="text-right">{{ formatNumber(result.rho) }}</td>
            <td class="text-right">{{ formatPValue(result.rho_p) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Bias Results Table -->
    <div class="overflow-x-auto">
      <h2 class="text-xl font-bold mb-4">Bias Results (Sorted by t-value)</h2>
      <table class="table w-full">
        <thead>
          <tr class="bg-base-200">
            <th>Model</th>
            <th>Left/Right</th>
            <th>t-value</th>
            <th>p-value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in biasResults" :key="result.model" class="hover">
            <td class="font-mono text-sm">{{ result.model }}</td>
            <td class="text-right">{{ result.left_n }}/{{ result.right_n }}</td>
            <td class="text-right">{{ formatNumber(result.t) }}</td>
            <td class="text-right">{{ formatPValue(result.t_p) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
</style>