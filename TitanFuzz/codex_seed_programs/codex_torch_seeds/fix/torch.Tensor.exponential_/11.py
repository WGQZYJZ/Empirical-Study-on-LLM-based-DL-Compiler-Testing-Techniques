'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exponential_\ntorch.Tensor.exponential_(_input_tensor, lambd=1, *, generator=None)\n'
import numpy as np
import torch
input_tensor = np.random.rand(2, 3)
print('Input data: ', input_tensor)
output_tensor = torch.Tensor.exponential_(input_tensor, lambd=1, generator=None)
print('Output data: ', output_tensor)