<script>
  import { fly } from "svelte/transition";
  import Title from "../shared/Title.svelte";
</script>

<div class="content" in:fly>
  <Title title={"Introduction"} />
  <p>
    Welcome to the Interactive Experience of Mathematics in Everyday Life! In
    this journey, we will explore how mathematical concepts are applied in
    practical situations.
  </p>

  <Title title={"Shopping"} />
  <p>
    Let's start by discussing how percentages are used when shopping. Imagine
    you come across a product with a 20% discount. How do you calculate the new
    price? (Formula: <span class="formula"
      >New Price = Original Price - (Discount Percentage * Original Price)</span
    >) Example: Suppose an item costs $100 and has a 20% discount. What is the
    final price? (Calculation:
    <span class="formula">New Price = $100 - (0.20 * $100) = $80</span>)
  </p>

  <Title title={"Data Analysis (Continuation)"} />
  <p>
    In addition to the mean, explore other relevant statistics such as median,
    mode, and standard deviation. How can these measures provide a more complete
    understanding of the data?
  </p>

  <Title title={"Proportions and Scales"} />
  <p>
    How are proportions applied in the real world? Explore situations where
    proportions are used, such as calculating recipes for a different number of
    servings.
  </p>

  <Title title={"Interest and Investments"} />
  <p>
    Understand how interest calculations are crucial in investments. Calculate
    simple and compound interest and explore their impact over time.
  </p>

  <Title title={"Geometry in Everyday Life"} />
  <p>
    Discover how geometric concepts are applied in practical situations, from
    calculating land areas to determining the amount of material needed for
    construction projects.
  </p>

  <Title title={"Probability in Everyday Events"} />
  <p>
    Understand how probability is used in everyday events, such as weather
    forecasts, travel planning, or in games of chance.
  </p>

  <Title title={"Conclusion"} />
  <p>
    Congratulations! You have explored a variety of practical ways to apply
    mathematical concepts in everyday life. Continue exploring and practicing to
    strengthen your mathematical skills in various real-world situations.
  </p>
</div>

<style>
  .content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: justify;
    padding: 20px;
  }

  .content > p {
    font-size: 20px;
    padding: 2rem;
  }

  .formula {
    font-family: "Courier New", Courier, monospace;
    background-color: #f0f0f0;
    padding: 2px 4px;
    border-radius: 4px;
  }
</style>
