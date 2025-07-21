'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos_\ntorch.Tensor.cos_(_input_tensor)\n'
import torch
import math
input_tensor = torch.randn(5, 5)
print(input_tensor)
torch.Tensor.cos_(input_tensor)
print(input_tensor)
cos_tensor = torch.cos(input_tensor)
print(cos_tensor)
print(torch.eq(cos_tensor, input_tensor))