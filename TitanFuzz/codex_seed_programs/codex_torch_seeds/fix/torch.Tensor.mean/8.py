'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mean\ntorch.Tensor.mean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input tensor:', input_tensor)
output_tensor = input_tensor.mean(dim=0, keepdim=False)
print('output tensor:', output_tensor)