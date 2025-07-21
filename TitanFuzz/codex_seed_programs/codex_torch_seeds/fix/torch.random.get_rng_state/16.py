'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.get_rng_state\ntorch.random.get_rng_state()\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
print(torch.random.get_rng_state())