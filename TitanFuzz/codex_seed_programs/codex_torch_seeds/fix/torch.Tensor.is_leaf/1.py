'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_leaf\ntorch.Tensor.is_leaf(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(4, 4)
print(torch.Tensor.is_leaf(_input_tensor))