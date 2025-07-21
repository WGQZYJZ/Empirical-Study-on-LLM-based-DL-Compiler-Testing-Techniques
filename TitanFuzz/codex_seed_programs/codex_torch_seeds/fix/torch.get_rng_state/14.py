'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
input_data = torch.randn(1, 3)
print(input_data)
torch.get_rng_state()