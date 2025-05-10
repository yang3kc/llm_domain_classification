<script setup>
import { ref, onMounted, computed } from 'vue'

const totalNumberOfDomains = 5653
const results = ref([])
const correlationResults = computed(() => {
  return results.value
    .map(result => ({
      model_name: result.model_name,
      n: result.n,
      rho: result.rho,
      rho_p: result.rho_p,
      company: result.company
    }))
    .sort((a, b) => b.rho - a.rho) // Sort by rho in descending order
})

const biasResults = computed(() => {
  let biasResults_internal = results.value
    .map(result => ({
      model_name: result.model_name,
      left_n: result.left_n,
      right_n: result.right_n,
      t: result.t,
      t_p: result.t_p,
      company: result.company
    }))
    .sort((a, b) => a.t - b.t) // Sort by t in ascending order
  biasResults_internal.forEach(result => {
    if (result.t < 0 && result.t_p < 0.05) {
      result.bias = 'left'
    } else if (result.t > 0 && result.t_p < 0.05) {
      result.bias = 'right'
    } else {
      result.bias = 'neutral'
    }
  })
  return biasResults_internal
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
const formatNumber = (num) => Number(num).toFixed(2)
const formatPercentage = (num) => (num / totalNumberOfDomains * 100).toFixed(1)
const formatBias = (bias) => {
  if (bias === 'left') return 'L+'
  if (bias === 'right') return 'R+'
  return 'N'
}

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
    <h1 class="text-3xl text-center font-bold my-6">Accuracy and political bias of news source credibility ratings by large language models</h1>
    <h2 class="text-xl text-center font-bold mb-4">Accuracy (measured by correlation with human expert ratings)</h2>
    <div class="rounded-box border border-base-content/5 bg-base-100">
      <table class="table table-zebra w-full">
        <thead>
          <tr class="bg-base-200">
            <th>
              Model
              <div class="tooltip tooltip-right" data-tip="Large Language Model variant used for testing">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              N (%)
              <div class="tooltip tooltip-right" data-tip="Number of domains processed by the model (percentage of total domains)">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              Spearman's ρ
              <div class="tooltip tooltip-left" data-tip="Spearman's rank correlation coefficient between model predictions and human expert ratings. The stars indicate the significance level of the correlation coefficient: *** p < 0.001, ** p < 0.01, * p < 0.05, NS p >= 0.05">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              Company
              <div class="tooltip tooltip-right" data-tip="Company that developed the model">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in correlationResults" :key="result.model_name" class="hover">
            <td class="font-mono text-sm">{{ result.model_name }}</td>
            <td class="text-right">{{ result.n }}({{ formatPercentage(result.n) }}%)</td>
            <td class="text-right">
              {{ formatNumber(result.rho) }}
              <span class="badge badge-info-content badge-outline badge-sm ml-1 opacity-40 cursor-help">{{ formatPValue(result.rho_p) }} </span>
            </td>
            <td class="text-right">{{ result.company }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Bias Results Table -->
    <h2 class="text-xl text-center font-bold mb-4">Bias measurement</h2>
    <div class="rounded-box border border-base-content/5 bg-base-100">
      <table class="table table-zebra w-full">
        <thead>
          <tr class="bg-base-200">
            <th>
              Model
              <div class="tooltip tooltip-right" data-tip="Large Language Model variant used for testing">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              Left | Right
              <div class="tooltip tooltip-right" data-tip="Number of domains classified as left-leaning vs right-leaning and processed by the model">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              t-statistic
              <div class="tooltip tooltip-left" data-tip="T-statistic measuring the bias between left and right classifications. Negative t-values indicate left-leaning bias, positive t-values indicate right-leaning bias. The stars indicate the significance level of the t-statistic: *** p < 0.001, ** p < 0.01, * p < 0.05, NS p >= 0.05">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
            <th class="text-right">
              Company
              <div class="tooltip tooltip-right" data-tip="Company that developed the model">
                <span class="text-xs ml-1 opacity-50 cursor-help">?</span>
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in biasResults" :key="result.model_name" class="hover">
            <td class="font-mono text-sm">{{ result.model_name }}</td>
            <td class="text-right">
                <div class="flex justify-end items-center gap-2">
                    <span class="text-info-content">{{ result.left_n }}</span>
                    <span class="opacity-50">|</span>
                    <span class="text-error-content">{{ result.right_n }}</span>
                </div>
            </td>
            <td class="text-right" :class="result.bias === 'left' ? 'text-info-content' : result.bias === 'right' ? 'text-error-content' : ''">
              {{ formatNumber(result.t) }}
              <span class="badge badge-info-content badge-outline badge-sm ml-1 opacity-40 cursor-help">{{ formatPValue(result.t_p) }} </span>
              <span class="badge badge-info-content badge-outline badge-sm ml-1 opacity-40 cursor-help">{{ formatBias(result.bias) }}</span>
            </td>
            <td class="text-right">{{ result.company }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
/* Custom tooltip styling */
:deep(.tooltip) {
  --tooltip-color: #1f2937; /* Dark background */
  --tooltip-text-color: white; /* White text */
}

:deep(.tooltip::before) {
  background-color: var(--tooltip-color) !important;
  color: var(--tooltip-text-color) !important;
  padding: 0.5rem 0.75rem !important;
  font-size: 0.875rem !important;
  max-width: 20rem !important;
  border-radius: 0.375rem !important;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
}
</style>