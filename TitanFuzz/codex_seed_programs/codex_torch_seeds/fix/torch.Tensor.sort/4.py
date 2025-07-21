'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input tensor: \n{}'.format(input_tensor))
output_tensor = input_tensor.sort(dim=(- 1), descending=False)
print('Output tensor: \n{}'.format(output_tensor))