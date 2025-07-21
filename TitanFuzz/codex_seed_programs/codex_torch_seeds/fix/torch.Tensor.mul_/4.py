'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mul_\ntorch.Tensor.mul_(_input_tensor, value)\n'
import torch
import numpy as np
_input_tensor = torch.rand(2, 3)
torch.Tensor.mul_(_input_tensor, 10)
print(_input_tensor)