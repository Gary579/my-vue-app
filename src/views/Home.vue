<template>
  <div class="home">
    <h2>{{ $t('home.greeting') }}</h2>
    <p>{{ $t('home.welcome') }}</p>
    <button>{{ $t('home.logout') }}</button>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>