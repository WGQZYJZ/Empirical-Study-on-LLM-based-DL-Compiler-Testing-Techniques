'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
x = torch.rand(2, 3)
print(x)
torch.random.set_rng_state(torch.get_rng_state())
print(torch.rand(2, 3))