<template>
  <div class="login">
    <h1>{{ $t('login.welcome') }}</h1>
    <p>{{ $t('login.instruction') }}</p>
    <form>
      <input type="text" :placeholder="$t('login.username')" />
      <input type="password" :placeholder="$t('login.password')" />
      <button>{{ $t('login.submit') }}</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginPage'
}
</script>