'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.kthvalue\ntorch.Tensor.kthvalue(_input_tensor, k, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('Input data:', input_tensor)
k = 2
dim = 1
keepdim = True
output_tensor = input_tensor.kthvalue(k, dim, keepdim)
print('Output data:', output_tensor)