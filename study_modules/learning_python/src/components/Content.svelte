<script>
    import { fly } from 'svelte/transition'
</script>

<div class="python-history" in:fly>
    <math>
        H(s) = ∫<sub>0</sub><sup>∞</sup> e<sup>-st</sup> h(t) dt
    </math> 
</div>

<style>
    .python-history{
        text-align: center;
    }
</style>