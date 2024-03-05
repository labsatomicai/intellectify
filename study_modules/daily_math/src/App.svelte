<script>

	import Header from "./components/Header.svelte";
	import Button from "./shared/Button.svelte";
	import Content from "./components/Content.svelte";

	let show_content = false;

	const handle_content = () => {
		show_content = !show_content;
	}
	
</script>
<Header/>
<main>
	<Button button_text="Start" on:click|once={handle_content}/>
</main>
{#if show_content === true}
	<Content/>
{/if}

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>