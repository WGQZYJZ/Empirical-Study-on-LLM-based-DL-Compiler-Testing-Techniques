'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(20, 10)
print(input_tensor.argmin(dim=1))
print(input_tensor.argmin(dim=0))
print(input_tensor.argmin(dim=1, keepdim=True))
print(input_tensor.argmin(dim=0, keepdim=True))