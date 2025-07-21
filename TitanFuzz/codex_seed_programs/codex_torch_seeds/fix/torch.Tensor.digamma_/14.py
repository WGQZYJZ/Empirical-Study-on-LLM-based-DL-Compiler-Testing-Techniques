'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma_\ntorch.Tensor.digamma_(_input_tensor)\n'
import torch
import math
input_tensor = torch.rand(1, 2, 3)
print(input_tensor)
result = torch.Tensor.digamma_(input_tensor)
print(result)