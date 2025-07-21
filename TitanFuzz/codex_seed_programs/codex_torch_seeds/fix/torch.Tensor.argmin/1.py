'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmin\ntorch.Tensor.argmin(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
result = input_tensor.argmin(dim=None, keepdim=False)
print(result)