import os
from cmdstanpy import CmdStanModel

######## Compiling the model ###########
stan_file = os.path.join('bernoulli.stan')
model = CmdStanModel(stan_file=stan_file)
# print(model)
# print(model.exe_info())

######## Fitting the model ##########
data_file = os.path.join('bernoulli.data.json')
fit = model.sample(data=data_file, output_dir="./outputs/")
