'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanquantile\ntorch.Tensor.nanquantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input tensor: ', input_tensor)
result_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)
print('Result tensor: ', result_tensor)