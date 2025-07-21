'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_rng_state\ntorch.get_rng_state()\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.get_rng_state())
'\nTask 4: Call the API torch.set_rng_state\ntorch.set_rng_state(rng_state)\n'
rng_state = torch.get_rng_state()
print(torch.randn(2, 3))
torch.set_rng_state(rng_state)
print(torch.randn(2, 3))
'\nTask 5: Call the API torch.manual_seed\n'
print(torch.randn(2, 3))
print(torch.randn(2, 3))