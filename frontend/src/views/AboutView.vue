<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { useCompanyLogos } from '@/composables/useCompanyLogos'

const { companyLogos } = useCompanyLogos()
</script>

<template>
  <div>
    <NavBar />
    <div class="container mx-auto">
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
          See <router-link to="/paper-rating" class="link link-neutral">Paper</router-link> page for more details.
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