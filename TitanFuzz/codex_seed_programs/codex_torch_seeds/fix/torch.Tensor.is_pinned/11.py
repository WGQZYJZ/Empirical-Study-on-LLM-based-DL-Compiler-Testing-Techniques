'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_pinned\ntorch.Tensor.is_pinned(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(5, 3)
print(_input_tensor.is_pinned())