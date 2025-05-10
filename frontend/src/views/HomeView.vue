<script setup>
import ModelResults from '@/components/ModelResults.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <div>
    <NavBar />
    <div class="container">
      <h1 class="text-3xl text-center font-bold my-6">LLM Domain Classification Results</h1>
      <ModelResults />
      <Footer />
    </div>
  </div>
</template>
