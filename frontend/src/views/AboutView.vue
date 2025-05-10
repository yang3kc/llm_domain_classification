<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <div>
    <NavBar />
    <div class="container mx-auto">
      <h1 class="text-3xl text-center font-bold my-6">The LLM Domain Classification project</h1>
      <p>
        This project aims to evaluate <strong>LLMs' ability to recognize and classify news sources into different categories</strong>.
        LLMs are increasingly used as information curators in our daily lives, thus their knowledge of news sources is crucial to the quality of the information they provide us.
      </p>
      <p>
        To answer this question, we use a pre-defined list of news domains with credibility ratings produced by human experts as our ground truth.
        We further test LLMs from different providers on this task and evaluate their performance.
        We also measure the <strong>political bias</strong> of LLMs on this task by comparing the ratings of the the models on the left-leaning and right-leaning domains.
      </p>
      <p>
        See <router-link to="/" class="link link-neutral">Results</router-link> page for the results.
        See <router-link to="/paper-rating" class="link link-neutral">Paper Rating</router-link> page for more details.
      </p>

    </div>
    <Footer />
  </div>
</template>