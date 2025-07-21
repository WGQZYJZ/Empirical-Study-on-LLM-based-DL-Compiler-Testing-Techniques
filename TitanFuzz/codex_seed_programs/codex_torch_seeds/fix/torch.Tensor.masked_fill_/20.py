'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
import numpy as np
input_tensor = torch.randn(3, 4)
print('input_tensor: ', input_tensor)
mask = (input_tensor > 0.5)
print('mask: ', mask)
input_tensor.masked_fill_(mask, 0)
print('input_tensor: ', input_tensor)