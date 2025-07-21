'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(5, 3)
print(_input_tensor)
print(torch.Tensor.all(_input_tensor))
print(torch.Tensor.all(_input_tensor, dim=0))
print(torch.Tensor.all(_input_tensor, dim=1))
print(torch.Tensor.all(_input_tensor, dim=0, keepdim=True))
print(torch.Tensor.all(_input_tensor, dim=1, keepdim=True))