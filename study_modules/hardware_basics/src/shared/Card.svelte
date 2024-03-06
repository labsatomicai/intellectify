<script>
    import * as feather from 'feather-icons';
    export let card_title;
    let icon;
  
    switch (card_title.toLowerCase()) {
      case 'power supply':
        icon = 'power';
        break;
      case 'motherboard':
        icon = 'settings';
        break;
      case 'cpu':
        icon = 'cpu';
        break;
      case 'coolers & fans':
        icon = 'wind';
        break;
      case 'ram':
        icon = 'hash';
        break;
      case 'graphics card':
        icon = 'monitor';
        break;
      case 'wi-fi board':
        icon = 'wifi';
        break;
      case 'hds and ssds':
        icon = 'hard-drive';
        break;
      default:
        icon = 'help-circle'; // Ícone padrão para títulos desconhecidos
    }
  </script>
  
  <div class="card">
    {#if icon in feather.icons}
      <div class="icon">{@html feather.icons[icon].toSvg()}</div>
    {/if}
    <h1>{card_title}</h1>
    <slot></slot>
  </div>
  
  <style>
    .card {
      display: flex;
      justify-content: center;
      flex-direction: column;
      align-items: center;
      background: #ffffff;
      padding: 20px;
      margin: 1rem;
      width: 20em;
      border-radius: 6px;
      box-shadow: 0px 2px 4px rgba(0, 0, 0, .3);
    }
  
    .icon {
      margin-bottom: 10px; /* Adiciona espaço entre o ícone e o título */
    }
  </style>
  