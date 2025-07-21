'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.min\ntorch.Tensor.min(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(4, 3)
print(input_tensor.min(dim=0, keepdim=True))
print(input_tensor.min(dim=1, keepdim=True))