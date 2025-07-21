'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(4, 3)
result = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('result: ', result)