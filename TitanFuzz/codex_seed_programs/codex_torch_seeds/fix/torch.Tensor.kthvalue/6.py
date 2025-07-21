'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.kthvalue\ntorch.Tensor.kthvalue(_input_tensor, k, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(10, 10)
print('Input tensor: ', input_tensor)
k = 2
dim = 0
keepdim = False
output_tensor = torch.Tensor.kthvalue(input_tensor, k, dim, keepdim)
print('Output tensor: ', output_tensor)