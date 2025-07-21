'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nanmean\ntorch.Tensor.nanmean(_input_tensor, dim=None, keepdim=False, *, dtype=None)\n'
import torch
import torch
_input_tensor = torch.randn(100, 100, 100)
_input_tensor[(_input_tensor > 0.5)] = float('nan')
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=2)
print(_output_tensor)