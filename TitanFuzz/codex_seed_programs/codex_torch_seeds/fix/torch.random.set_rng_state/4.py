'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
x = torch.randn(1, requires_grad=True)
torch.random.set_rng_state(torch.get_rng_state())
y = torch.randn(1, requires_grad=True)
print(x)
print(y)