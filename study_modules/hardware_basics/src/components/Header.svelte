<script>
</script>

<header>
  <div class="logo-container">
    <img width="130" src="/img/neurahub_logo_no_bg.png" alt="" />
  </div>
  <div class="title-logo-wrapper">
    <div class="game-title">
      <h1>Hardware basics</h1>
      <div class="powered">
        <p>Powered by perceptrawave</p>
        <img class="logo" width="100" src="/img/perceptrawave.png" alt="" />
      </div>
    </div>
    <slot></slot>
  </div>
</header>
<style>
    .title-logo-wrapper {
      background-image: url("/img/banner.png");
      width: 100%;
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      height: 50vh;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
  
    .game-title > h1 {
      font-size: 3rem;
      text-align: center;
      color: #f8f8f8;
      margin: 0;
    }
  
    .powered {
      display: flex;
      align-items: center;
      justify-content: center;
      color: #f8f8f8;
      margin: 0;
    }
  
    .logo-container{
      padding: 1.5rem;
    }
  
    @media only screen and (max-width: 600px) {
      header {
        padding: 1rem;
      }
  
      .game-title > h1 {
        font-size: 2rem;
      }
    }
  </style>