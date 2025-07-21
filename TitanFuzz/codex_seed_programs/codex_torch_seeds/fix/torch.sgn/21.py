'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
import torch
input_data = torch.randn(10, 10)
print(input_data)
output_data = torch.sgn(input_data)
print(output_data)