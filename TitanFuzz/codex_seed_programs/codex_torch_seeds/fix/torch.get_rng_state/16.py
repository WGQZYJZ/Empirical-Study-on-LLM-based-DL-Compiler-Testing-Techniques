'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
input = torch.randn(2, 3)
print(input)
print(torch.get_rng_state())
torch.set_rng_state(torch.get_rng_state())
print(torch.get_rng_state())
input = torch.randn(2, 3)
print(input)