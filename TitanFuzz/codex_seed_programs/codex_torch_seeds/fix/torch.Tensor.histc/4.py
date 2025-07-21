'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
import numpy as np
input_tensor = torch.randn(100, 3)
print('input_tensor: {}'.format(input_tensor))
histc_result = input_tensor.histc(bins=100, min=0, max=0)
print('histc_result: {}'.format(histc_result))