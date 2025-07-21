'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sort\ntorch.Tensor.sort(_input_tensor, dim=-1, descending=False)\n'
import torch
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:', _input_tensor)
torch.Tensor.sort(_input_tensor, dim=(- 1), descending=False)
print('Output tensor:', _input_tensor)