'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_meta\ntorch.Tensor.is_meta(_input_tensor, )\n'
import torch
_input_tensor = torch.rand((1, 3, 4, 5))
print(torch.Tensor.is_meta(_input_tensor))