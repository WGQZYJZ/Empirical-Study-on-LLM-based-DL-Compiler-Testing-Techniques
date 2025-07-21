'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print(torch.Tensor.all(input_tensor, dim=None, keepdim=False))
print(torch.Tensor.all(input_tensor, dim=0, keepdim=False))
print(torch.Tensor.all(input_tensor, dim=1, keepdim=False))
print(torch.Tensor.all(input_tensor, dim=None, keepdim=True))
print(torch.Tensor.all(input_tensor, dim=0, keepdim=True))
print(torch.Tensor.all(input_tensor, dim=1, keepdim=True))