'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
x = torch.randn(1)
y = torch.randn(1)
print(x, y)
torch.set_rng_state(torch.get_rng_state())
print(torch.randn(1), torch.randn(1))