'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_pinned\ntorch.Tensor.is_pinned(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(size=(10, 10), dtype=torch.float32)
print('The tensor is pinned: ', _input_tensor.is_pinned())