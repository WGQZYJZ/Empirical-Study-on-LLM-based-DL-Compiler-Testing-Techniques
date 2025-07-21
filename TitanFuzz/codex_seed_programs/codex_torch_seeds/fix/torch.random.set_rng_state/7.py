'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
x = torch.rand(4, 4)
state = torch.get_rng_state()
torch.random.set_rng_state(state)
y = torch.rand(4, 4)
print(x)
print(y)
print((x == y))