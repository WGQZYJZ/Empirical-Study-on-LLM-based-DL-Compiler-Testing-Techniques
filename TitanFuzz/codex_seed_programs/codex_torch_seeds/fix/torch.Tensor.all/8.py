'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
print(_input_tensor.all())
print(_input_tensor.all(dim=0))
print(_input_tensor.all(dim=1))
print(_input_tensor.all(dim=1, keepdim=True))