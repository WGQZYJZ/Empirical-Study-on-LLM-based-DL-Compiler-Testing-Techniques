'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
import torch
input_data = torch.randn(1, 1, 2)
torch.set_rng_state(torch.get_rng_state())
print(torch.randn(1, 1, 2))
print(torch.randn(1, 1, 2))