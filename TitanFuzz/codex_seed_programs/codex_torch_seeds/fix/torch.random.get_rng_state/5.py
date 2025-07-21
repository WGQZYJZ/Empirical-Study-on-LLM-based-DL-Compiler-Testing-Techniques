'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.get_rng_state\ntorch.random.get_rng_state()\n'
import torch
input = torch.randn(2, 3)
print('Input:', input)
print('RNG State:', torch.random.get_rng_state())