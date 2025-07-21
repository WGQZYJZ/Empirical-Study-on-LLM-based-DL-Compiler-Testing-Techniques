'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
result = torch.Tensor.subtract_(input_tensor, other)
print(result)