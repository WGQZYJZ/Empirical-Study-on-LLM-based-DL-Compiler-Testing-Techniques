'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
import numpy as np
np.random.seed(0)
torch.set_rng_state(torch.get_rng_state())
x = torch.randn(2, 3)
print(x)
torch.set_rng_state(torch.get_rng_state())
y = torch.randn(2, 3)
print(y)