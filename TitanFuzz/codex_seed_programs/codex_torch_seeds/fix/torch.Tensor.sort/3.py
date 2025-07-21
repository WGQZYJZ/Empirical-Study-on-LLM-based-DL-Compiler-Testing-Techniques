'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.randn(4, 3)
print('input_tensor = ', input_tensor)
result_tensor = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)
print('result_tensor = ', result_tensor)
print('result_tensor = ', result_tensor)