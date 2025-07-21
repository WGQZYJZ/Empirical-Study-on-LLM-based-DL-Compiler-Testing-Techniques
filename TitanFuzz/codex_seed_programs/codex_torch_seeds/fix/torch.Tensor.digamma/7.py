'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
digamma_tensor = torch.Tensor.digamma(input_tensor)
print(digamma_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, _other_tensor, _p)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(3, 3)
other_tensor = torch.randn(3, 3)
print(input_tensor)
print(other_tensor)