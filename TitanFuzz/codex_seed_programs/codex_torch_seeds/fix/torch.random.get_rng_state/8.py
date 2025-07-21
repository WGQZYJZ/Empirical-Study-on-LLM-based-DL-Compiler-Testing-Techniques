'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.get_rng_state\ntorch.random.get_rng_state()\n'
import torch
input = torch.randn(20, 20)
torch.random.get_rng_state()
print('input: ', input)
print('torch.random.get_rng_state(): ', torch.random.get_rng_state())