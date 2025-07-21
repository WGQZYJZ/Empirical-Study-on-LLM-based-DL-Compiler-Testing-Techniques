'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 3)
print('input_tensor: ', input_tensor)
any_result = torch.Tensor.any(input_tensor, dim=None, keepdim=False)
print('any_result: ', any_result)