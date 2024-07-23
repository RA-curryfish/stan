data {
  int<lower=0> N; // lower limit???
  array[N] int<lower=0,upper=1> y; // data of 0s and 1s
}
parameters {
  real<lower=0,upper=1> theta; // probability of success
}
model {
  theta ~ beta(1,1); // uniform dist. between [0,1], a prior belief
  y ~ bernoulli(theta);
}
