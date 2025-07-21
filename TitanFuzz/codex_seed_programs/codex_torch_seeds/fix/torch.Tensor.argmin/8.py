'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
print(input_tensor.argmin())
print(input_tensor.argmin(dim=0))
print(input_tensor.argmin(dim=1))
print(input_tensor.argmin(dim=1, keepdim=True))