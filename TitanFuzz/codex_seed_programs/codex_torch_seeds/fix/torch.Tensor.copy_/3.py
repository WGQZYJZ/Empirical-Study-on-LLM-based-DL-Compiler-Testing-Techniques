'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
_input_tensor = torch.randn(2, 3)
src = torch.randn(2, 3)
torch.Tensor.copy_(_input_tensor, src, non_blocking=False)
print(_input_tensor)