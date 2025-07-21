'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
state = torch.get_rng_state()
x = torch.randn(1)
torch.set_rng_state(state)
y = torch.randn(1)
print(x)
print(y)