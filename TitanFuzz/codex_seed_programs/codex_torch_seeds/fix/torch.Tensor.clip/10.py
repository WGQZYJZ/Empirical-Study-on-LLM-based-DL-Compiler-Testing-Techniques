'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip\ntorch.Tensor.clip(_input_tensor, min=None, max=None)\n'
import torch
_input_tensor = torch.arange((- 5), 5, 0.1)
_output_tensor = torch.Tensor.clip(_input_tensor, min=(- 3), max=3)
print(_input_tensor)
print(_output_tensor)