<script>
  import Card from "../shared/Card.svelte";
  import * as feather from "feather-icons";
  import { fly }from 'svelte/transition';
</script>

<div class="content" in:fly>
  <div class="info-cards">
    <Card card_title={"Power supply"}>
      <p>Responsible for providing electrical power to the computer.</p>
    </Card>
    <Card card_title={"Motherboard"}>
      <p>Main circuit board that connects and controls various components.</p>
    </Card>
    <Card card_title={"CPU"}>
      <p>Central Processing Unit responsible for executing instructions.</p>
    </Card>
    <Card card_title={"Coolers & fans"}>
      <p>
        Keep components cool by dissipating heat generated during operation.
      </p>
    </Card>
    <Card card_title={"RAM"}>
      <p>Random Access Memory used for temporary storage of data.</p>
    </Card>
    <Card card_title={"Graphics card"}>
      <p>Responsible for rendering images and videos on the display.</p>
    </Card>
    <Card card_title={"Wi-fi board"}>
      <p>Enables wireless connectivity to networks.</p>
    </Card>
    <Card card_title={"HDs and SSDs"}>
      <p>Storage devices for data and applications.</p>
    </Card>
  </div>
</div>

<style>
  .content {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .info-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }

  @media only screen and (max-width: 600px) {
    .info-cards {
      grid-template-columns: 1fr;
    }
  }
</style>
