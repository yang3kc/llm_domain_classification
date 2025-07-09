<script setup>
import ModelResults from '@/components/ModelResults.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <div class="container mx-auto flex-grow">
      <ModelResults />
    </div>
    <Footer />
  </div>
</template>
