'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.get_rng_state())