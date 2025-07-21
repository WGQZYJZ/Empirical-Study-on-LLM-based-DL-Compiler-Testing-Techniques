'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copy_\ntorch.Tensor.copy_(_input_tensor, src, non_blocking=False)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
input_tensor.copy_(torch.arange(9).view(3, 3))
print(input_tensor)