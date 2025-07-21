'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn((2, 3, 3))
print(input_tensor)
print(torch.Tensor.median(input_tensor, dim=1, keepdim=True))
print(torch.Tensor.median(input_tensor, dim=1, keepdim=False))