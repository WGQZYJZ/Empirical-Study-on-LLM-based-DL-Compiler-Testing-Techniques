'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(_input_tensor)
result = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('Result:')
print(result)