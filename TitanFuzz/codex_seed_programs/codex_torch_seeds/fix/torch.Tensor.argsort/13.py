'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.argsort(input_tensor, dim=(- 1), descending=False)
print('Input tensor: ', input_tensor)
print('Output tensor: ', output_tensor)