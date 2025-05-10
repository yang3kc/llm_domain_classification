<template>
  <div class="navbar bg-base-100 border-b border-base-content/5">
    <div class="container mx-auto">
      <div class="flex-1">
        <a class="text-xl font-bold">LLM Domain Classification</a>
      </div>
      <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
          <li><a href="/" class="active">Results</a></li>
          <li><a href="/about">About</a></li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
}
</style>