'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print('Input tensor: \n', input_tensor)
result = torch.Tensor.sort(input_tensor, dim=(- 1), descending=False)
print('Result tensor: \n', result)