'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.prod\ntorch.Tensor.prod(_input_tensor, dim=None, keepdim=False, dtype=None)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
print(input_tensor.prod())
print(input_tensor.prod(dim=0))
print(input_tensor.prod(dim=1))
print(input_tensor.prod(dim=1, keepdim=True))