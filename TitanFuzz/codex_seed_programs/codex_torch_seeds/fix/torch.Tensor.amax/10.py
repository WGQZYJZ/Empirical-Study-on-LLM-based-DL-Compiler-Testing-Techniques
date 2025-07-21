'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amax\ntorch.Tensor.amax(_input_tensor, dim=None, keepdim=False)\n'
import torch
import numpy as np
input_tensor = torch.randn(4, 4)
print(input_tensor)
print(torch.Tensor.amax(input_tensor, dim=0, keepdim=False))
print(torch.Tensor.amax(input_tensor, dim=1, keepdim=False))
print(torch.Tensor.amax(input_tensor, dim=1, keepdim=True))