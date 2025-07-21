'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('\nInput Tensor: ', input_tensor)
output_tensor = input_tensor.sort(dim=(- 1), descending=False)
print('\nOutput Tensor: ', output_tensor)