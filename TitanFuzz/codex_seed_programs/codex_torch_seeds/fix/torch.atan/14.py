'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atan\ntorch.atan(input, *, out=None)\n'
import torch
input_data = torch.randn(10, 5)
output_data = torch.atan(input_data)
print('output_data = ', output_data)