'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix\ntorch.Tensor.fix(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(1, 3, 3)
torch.Tensor.fix(_input_tensor)
print('Input tensor: {}'.format(_input_tensor))
print('Input tensor shape: {}'.format(_input_tensor.shape))