'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
input_data = torch.randn(5, 5)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
print(prelu(input_data))