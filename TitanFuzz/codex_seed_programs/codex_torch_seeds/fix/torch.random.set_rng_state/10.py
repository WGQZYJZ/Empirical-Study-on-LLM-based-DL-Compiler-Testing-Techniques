'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
input_data = torch.randn(1, 3)
rng_state = torch.random.get_rng_state()
torch.random.set_rng_state(rng_state)
print(torch.randn(1, 3))
torch.random.set_rng_state(rng_state)
print(torch.randn(1, 3))