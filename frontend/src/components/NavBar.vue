<template>
  <div class="navbar bg-neutral border-b border-base-content/5">
    <div class="container mx-auto">
      <div class="flex-none">
        <ul class="menu menu-horizontal px-1">
          <li><a router-link="/" class="btn btn-neutral text-white text-xl">Results</a></li>
          <li><a router-link="/about" class="btn btn-neutral text-white text-xl">About</a></li>
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