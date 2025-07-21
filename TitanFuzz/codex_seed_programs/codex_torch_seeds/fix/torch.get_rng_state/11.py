'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
input_data = torch.randn(10)
print(input_data)
print(torch.get_rng_state())
'\nTask 4: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
torch.set_rng_state(torch.get_rng_state())
print(torch.randn(10))