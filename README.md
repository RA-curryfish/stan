# Probabilistic Programming

A repo to practice some prob. programming examples.

### CSV Headers
- lp__ - the total log probability density (up to an additive constant) at each sample
- accept_stat__ - the average Metropolis acceptance probability over each simulated Hamiltonian trajectory
- stepsize__ - integrator step size
- treedepth__ - depth of tree used by NUTS (NUTS sampler)
- n_leapfrog__ - number of leapfrog calculations (NUTS sampler)
- divergent__ - has value 1 if trajectory diverged, otherwise 0. (NUTS sampler)
- energy__ - value of the Hamiltonian
- int_time__ - total integration time (static HMC sampler)
- (model parameters follow)
  
Summarize csv results:
`~/.cmdstand/cmdstan-<version>/bin/stansummary <file1.csv> .... <filen.csv>`
