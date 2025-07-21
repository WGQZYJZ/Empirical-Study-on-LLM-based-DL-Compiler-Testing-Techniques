'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.get_rng_state\ntorch.random.get_rng_state()\n'
import torch
x = torch.randn(1)
print(x)
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())
torch.random.manual_seed(1)
torch.random.initial_seed()
torch.random.get_rng_state()
torch.random.set_rng_state(torch.random.get_rng_state())