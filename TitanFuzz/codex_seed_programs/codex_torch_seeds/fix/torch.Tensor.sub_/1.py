'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
torch.Tensor.sub_(input_tensor, other, alpha=1)
print(input_tensor)
print(other)