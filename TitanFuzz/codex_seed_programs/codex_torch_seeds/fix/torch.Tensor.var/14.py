'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 5)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.var(dim=1, unbiased=False, keepdim=True)
print('output_tensor:', output_tensor)