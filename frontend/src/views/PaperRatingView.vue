<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { ref } from 'vue'

const bibtex = `@inproceedings{yang2025accuracy,
    author = {Yang, Kai-Cheng and Menczer, Filippo},
    title = {Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models},
    year = {2025},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3717867.3717903},
    doi = {10.1145/3717867.3717903},
    booktitle = {Proceedings of the 17th ACM Web Science Conference 2025},
    pages = {127–137},
    numpages = {11},
    series = {Websci '25}
}`

const copySuccess = ref(false)

const copyToClipboard = async () => {
  try {
    await navigator.clipboard.writeText(bibtex)
    copySuccess.value = true
    setTimeout(() => {
      copySuccess.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy text: ', err)
  }
}
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <NavBar />
    <div class="container mx-auto flex-grow">
      <!-- title  -->
      <div class="prose-h1 prose-2xl prose-slate text-center font-bold mt-6">Accuracy and political bias of news source credibility ratings by large language models</div>
      <!-- authors -->
      <div class="prose prose-xl text-center prose-slate max-w-none my-4">
         <a href="https://www.kaichengyang.me" class="link link-neutral" target="_blank">Kai-Cheng Yang</a> and <a href="https://cnets.indiana.edu/fil" class="link link-neutral" target="_blank">Filippo Menczer</a>
      </div>
      <!-- links -->
      <div class="text-center my-8">
        <div class="inline-flex flex-wrap gap-4 justify-center">
          <a href="https://doi.org/10.1145/3717867.3717903" class="btn btn-outline border-neutral text-neutral hover:bg-neutral hover:text-white text-lg" target="_blank">
            <font-awesome-icon :icon="['fas', 'file-pdf']" class="mr-2" /> DOI
          </a>
          <a href="https://arxiv.org/abs/2304.00228" class="btn btn-outline border-neutral text-neutral hover:bg-neutral hover:text-white text-lg" target="_blank">
            <font-awesome-icon :icon="['fas', 'file-pdf']" class="mr-2" /> arXiv
          </a>
          <a href="https://github.com/osome-iu/llm_domain_rating" class="btn btn-outline border-neutral text-neutral hover:bg-neutral hover:text-white text-lg" target="_blank">
            <font-awesome-icon :icon="['fab', 'github']" class="mr-2" /> GitHub
          </a>
          <a href="https://x.com/yang3kc/status/1823404980126261262" class="btn btn-outline border-neutral text-neutral hover:bg-neutral hover:text-white text-lg" target="_blank">
            <font-awesome-icon :icon="['fab', 'x-twitter']" class="mr-2" /> Twitter
          </a>
        </div>
      </div>
      <!-- abstract -->
      <div class="prose-h2 prose-xl prose-slate text-center font-bold my-4">Abstract</div>
      <div class="prose prose prose-slate max-w-none my-4">
        <p>
        Search engines increasingly leverage large language models (LLMs) to generate direct answers, and AI chatbots now access the Internet for fresh data.
        As information curators for billions of users, LLMs must assess the accuracy and reliability of different sources.
        This paper audits nine widely used LLMs from three leading providers-OpenAI, Google, and Meta-to evaluate their ability to discern credible and high-quality information sources from low-credibility ones.
        We find that while LLMs can rate most tested news outlets, larger models more frequently refuse to provide ratings due to insufficient information, whereas smaller models are more prone to making errors in their ratings.
        For sources where ratings are provided, LLMs exhibit a high level of agreement among themselves (average Spearman's 𝜌 = 0.79), but their ratings align only moderately with human expert evaluations (average 𝜌 = 0.50).
        Analyzing news sources with different political leanings in the US, we observe a liberal bias in credibility ratings yielded by all LLMs in default configurations. Additionally, assigning partisan roles to LLMs consistently induces strong politically congruent bias in their ratings.
        These findings have important implications for the use of LLMs in curating news and political information.
        </p>
      </div>
      <!-- bib -->
      <div class="prose-h2 prose-xl prose-slate text-center font-bold my-4">Bibtex</div>
      <div class="prose prose prose-slate max-w-none my-4 relative bibtex-container">
        <button
          @click="copyToClipboard"
          class="btn btn-sm btn-neutral absolute top-2 right-2"
          :class="{ 'btn-success': copySuccess }"
        >
          <font-awesome-icon :icon="['fas', 'copy']" class="mr-2" />
          {{ copySuccess ? 'Copied!' : 'Copy' }}
        </button>
        <pre><code class="text-neutral">{{ bibtex }}</code></pre>
      </div>
    </div>
    <Footer />
  </div>
</template>

<style scoped>
pre {
  position: relative;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 0.5rem;
  overflow-x: auto;
}

code {
  font-family: monospace;
  white-space: pre;
}

.bibtex-container .btn {
  z-index: 10;
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
}
</style>