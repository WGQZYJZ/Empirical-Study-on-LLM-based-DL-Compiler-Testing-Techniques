'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
import numpy as np
input_data = torch.rand(10)
print(f'input_data: {input_data}')
print(f'random_state: {torch.get_rng_state()}')
'\nTask 1: Call torch.set_rng_state\nTask 2: Call torch.get_rng_state\n'
random_state = torch.get_rng_state()
torch.set_rng_state(random_state)
print(f'random_state: {torch.get_rng_state()}')