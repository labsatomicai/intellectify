<script>
    export let button_text;
 </script>
 
 <button on:click>
    {button_text}
 </button>
 
 <style>
   button{
      border: 2px solid #007bff;
      color: #f8f8f8;
      border-radius: 30px;
      width: 200px;
      font-size: 16px;
      font-weight: bold;
      background-color: transparent;
   }

   button:hover{
      color: #f8f8f8;
      background: #007bff;
      transition: linear .3s;
      cursor: pointer;
   }
 </style>