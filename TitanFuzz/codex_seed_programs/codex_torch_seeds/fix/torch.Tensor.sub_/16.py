'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
result = torch.Tensor.sub_(input_tensor, other)
print(result)