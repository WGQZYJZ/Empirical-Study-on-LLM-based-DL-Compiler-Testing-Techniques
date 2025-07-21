'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
result = torch.sgn(input_data)
print(result)