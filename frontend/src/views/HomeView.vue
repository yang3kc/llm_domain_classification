<script setup>
import ModelResults from '@/components/ModelResults.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <div class="container mx-auto py-8">
    <NavBar />
    <h1 class="text-3xl font-bold mb-6">LLM Domain Classification Results</h1>
    <ModelResults />
    <Footer />
  </div>
</template>
