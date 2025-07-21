'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
output_data = torch.rsqrt(input_data)
print('Input data:', input_data)
print('Output data:', output_data)