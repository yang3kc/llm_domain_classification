<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <div>
    <NavBar />
    <div class="container mx-auto">
      <div class="prose-h1 prose-2xl prose-slate text-center font-bold mt-6">Accuracy and political bias of news source credibility ratings by large language models</div>
      <div class="prose prose-xl text-center prose-slate max-w-none my-4">
         <a href="https://www.kaichengyang.me" class="link link-neutral" target="_blank">Kai-Cheng Yang</a> and <a href="https://cnets.indiana.edu/fil" class="link link-neutral" target="_blank">Filippo Menczer</a>
      </div>
      <div class="flex justify-center gap-4 my-8">
        <div class="btn btn-neutral btn-outline">
          <a href="https://arxiv.org/abs/2304.00228" class="text-neutral" target="_blank">
            <font-awesome-icon :icon="['fas', 'file-pdf']" class="mr-2" /> arXiv
          </a>
        </div>
        <div class="btn btn-neutral btn-outline">
          <a href="https://github.com/osome-iu/llm_domain_rating" class="text-neutral" target="_blank">
            <font-awesome-icon :icon="['fab', 'github']" class="mr-2" /> GitHub
          </a>
        </div>
        <div class="btn btn-neutral btn-outline">
          <a href="https://x.com/yang3kc/status/1823404980126261262" class="text-neutral" target="_blank">
            <font-awesome-icon :icon="['fab', 'x-twitter']" class="mr-2" /> Twitter thread
          </a>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>