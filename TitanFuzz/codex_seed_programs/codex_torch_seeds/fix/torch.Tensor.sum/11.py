'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum\ntorch.Tensor.sum(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.sum(_input_tensor, dim=1, keepdim=False, dtype=None)
print(_output_tensor)