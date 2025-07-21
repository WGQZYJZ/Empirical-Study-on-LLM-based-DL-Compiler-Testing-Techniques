'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
x = torch.randn(1, requires_grad=True)
print(x)
torch.get_rng_state()
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
x = torch.randn(1, requires_grad=True)
print(x)
torch.set_rng_state(torch.get_rng_state())
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.manual_seed\n'
import torch