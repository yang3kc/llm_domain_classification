<script setup>
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
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
    </div>
    <Footer />
  </div>
</template>