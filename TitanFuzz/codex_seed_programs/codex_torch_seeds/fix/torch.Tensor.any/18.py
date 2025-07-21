'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input Tensor: \n', input_tensor)
result_tensor = torch.Tensor.any(input_tensor, dim=None, keepdim=False)
print('Result Tensor: \n', result_tensor)