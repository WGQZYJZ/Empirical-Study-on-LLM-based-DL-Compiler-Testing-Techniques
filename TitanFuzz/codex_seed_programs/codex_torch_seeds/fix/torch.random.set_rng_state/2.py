'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
torch.random.set_rng_state(torch.get_rng_state())
output_data = torch.rand(2, 3)
print(output_data)
print((input_data == output_data))