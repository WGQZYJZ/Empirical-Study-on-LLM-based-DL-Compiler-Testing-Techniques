'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input_data = torch.rand(10)
print(input_data)
output_data = torch.hypot(input_data, input_data)
print(output_data)