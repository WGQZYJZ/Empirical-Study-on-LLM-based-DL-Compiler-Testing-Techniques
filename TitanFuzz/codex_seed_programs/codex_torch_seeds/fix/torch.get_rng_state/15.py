'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
data = torch.randn(1, 1)
rng_state = torch.get_rng_state()
print(rng_state)