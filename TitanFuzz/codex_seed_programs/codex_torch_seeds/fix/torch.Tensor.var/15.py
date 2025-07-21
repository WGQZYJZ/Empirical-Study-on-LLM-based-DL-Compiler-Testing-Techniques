'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input tensor:', input_tensor)
variance_0 = input_tensor.var(dim=0)
print('Variance along the 0th dimension:', variance_0)
variance_1 = input_tensor.var(dim=1)
print('Variance along the 1st dimension:', variance_1)