'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil_\ntorch.Tensor.ceil_(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.Tensor.ceil_(input_tensor)
print(input_tensor)