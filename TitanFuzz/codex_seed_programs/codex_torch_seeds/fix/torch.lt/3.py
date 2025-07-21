'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
import torch
input_data = torch.rand(3, 4)
print(input_data)
output_data = torch.lt(input_data, 0.5)
print(output_data)