'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
x = torch.rand(3, 3)
print(x)
rng_state = torch.get_rng_state()
y = torch.rand(3, 3)
print(y)
torch.set_rng_state(rng_state)
z = torch.rand(3, 3)
print(z)