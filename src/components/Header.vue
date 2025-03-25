<template>
  <header>
    <nav>
      <ul>
        <li><a href="#">{{ $t('nav.home') }}</a></li>
        <li><a href="#">{{ $t('nav.about') }}</a></li>
        <li><a href="#">{{ $t('nav.contact') }}</a></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>