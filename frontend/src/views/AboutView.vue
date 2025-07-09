<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { useCompanyLogos } from '@/composables/useCompanyLogos'

const { companyLogos } = useCompanyLogos()
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <div class="container mx-auto flex-grow">
      <div class="flex items-center gap-8 mb-8 justify-center">
        <div class="flex-shrink-0">
          <img :src="companyLogos.logo" alt="Logo" class="h-25 inline-block mt-5" />
        </div>
        <div class="flex-grow max-w-xl">
          <div class="prose-h1 prose-2xl prose-slate font-bold mt-5">The LLM Domain Classification project</div>
          <div class="prose prose-xl prose-slate max-w-none mt-2">Contact: <a href="https://www.kaichengyang.me" class="link link-neutral" target="_blank">Kai-Cheng Yang</a> <a href="mailto:yang3kc@gmail.com" class="link link-neutral"><font-awesome-icon :icon="['fas', 'envelope']" /></a></div>
        </div>
      </div>

      <article class="prose prose-slate max-w-none">
        <p>
          This project evaluates how well <strong>Large Language Models (LLMs) can assess the credibility and categorize news sources</strong>.
          As LLMs increasingly help curate and filter information in search engines, chatbots, and recommendation systems, their ability to accurately evaluate news sources directly impacts the quality and reliability of information they provide to users.
        </p>
        <p>
          To this end, we use a pre-defined list of news domains with <strong>credibility ratings</strong> produced by human experts as our ground truth.
          We further test LLMs from different providers on this task and evaluate their performance.
          We also measure the <strong>political bias</strong> of LLMs on this task by comparing the ratings of the the models on the left-leaning and right-leaning domains in the U.S. context.
          We will keep adding results for more models when they become available.
        </p>
        <p>
          See <router-link to="/" class="link link-neutral">Dashboard</router-link> page for the results and methods.
          See <router-link to="/paper-rating" class="link link-neutral">Paper</router-link> page for more details.
          Questions and requests can be sent to <a href="mailto:yang3kc@gmail.com" class="link link-neutral">Kai-Cheng Yang</a>.
        </p>
      </article>

      <div class="divider divider-neutral my-8"></div>

      <article class="prose prose-slate max-w-none">
        <div class="prose-h1 prose-2xl prose-slate font-bold mt-5 text-center">About this website</div>
        <p>
          This website uses <a href="https://vuejs.org/" class="link link-neutral" target="_blank">Vue.js</a> <a href="https://tailwindcss.com/" class="link link-neutral" target="_blank">Tailwind CSS</a>, <a href="https://daisyui.com/" class="link link-neutral" target="_blank">DaisyUI</a> and <a href="https://fontawesome.com/" class="link link-neutral" target="_blank">FontAwesome</a>.
          The source code was "vibe-coded" with <a href="https://www.cursor.com/" class="link link-neutral" target="_blank">Cursor</a>.
        </p>
      </article>

    </div>
    <Footer />
  </div>
</template>