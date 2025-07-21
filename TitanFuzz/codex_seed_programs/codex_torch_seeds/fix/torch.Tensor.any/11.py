'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.any(input_tensor, dim=None, keepdim=False)
print('output_tensor: ', output_tensor)