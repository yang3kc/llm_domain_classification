<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { ref } from 'vue'

const bibtex = `@misc{yang2024accuracy,
  title={Accuracy and political bias of news source credibility ratings by large language models},
  author={Kai-Cheng Yang and Filippo Menczer},
  year={2024},
  eprint={2304.00228},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2304.00228},
  journal={Forthcoming in the proceedings of ACM Web Science Conference; arXiv:2304.00228}
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
  <div>
    <NavBar />
    <div class="container mx-auto">
      <!-- title  -->
      <div class="prose-h1 prose-2xl prose-slate text-center font-bold mt-6">Accuracy and political bias of news source credibility ratings by large language models</div>
      <!-- authors -->
      <div class="prose prose-xl text-center prose-slate max-w-none my-4">
         <a href="https://www.kaichengyang.me" class="link link-neutral" target="_blank">Kai-Cheng Yang</a> and <a href="https://cnets.indiana.edu/fil" class="link link-neutral" target="_blank">Filippo Menczer</a>
      </div>
      <!-- links -->
      <div class="flex justify-center gap-4 my-4">
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
      <!-- abstract -->
      <div class="prose-h2 prose-xl prose-slate text-center font-bold my-4">Abstract</div>
      <div class="prose prose prose-slate max-w-none my-4">
        <p>
        Search engines increasingly leverage large language models (LLMs) to generate direct answers, and AI chatbots now access the Internet for fresh data.
        As information curators for billions of users, LLMs must assess the accuracy and reliability of different sources.
        This paper audits nine widely used LLMs from three leading providers-OpenAI, Google, and Meta—to evaluate their ability to discern credible and high-quality information sources from low-credibility ones.
        We find that while LLMs can rate most tested news outlets, larger models more frequently refuse to provide ratings due to insufficient information, whereas smaller models are more prone to making errors in their ratings.
        For sources where ratings are provided, LLMs exhibit a high level of agreement among them- selves (average Spearman's 𝜌 = 0.79), but their ratings align only moderately with human expert evaluations (average 𝜌 = 0.50).
        Analyzing news sources with different political leanings in the US, we observe a liberal bias in credibility ratings yielded by all LLMs in default configurations. Additionally, assigning partisan roles to LLMs consistently induces strong politically congruent bias in their ratings.
        These findings have important implications for the use of LLMs in curating news and political information.
        </p>
      </div>
      <!-- bib -->
      <div class="prose-h2 prose-xl prose-slate text-center font-bold my-4">Bibtex</div>
      <div class="prose prose prose-slate max-w-none my-4 relative">
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

.btn {
  z-index: 10;
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
}
</style>