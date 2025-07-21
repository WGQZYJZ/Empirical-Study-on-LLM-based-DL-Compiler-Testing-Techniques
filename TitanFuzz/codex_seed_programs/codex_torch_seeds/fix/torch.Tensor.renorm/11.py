'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm\ntorch.Tensor.renorm(_input_tensor, p, dim, maxnorm)\n'
import torch
import numpy as np
input_tensor = torch.arange(1, 13, dtype=torch.float).view(3, 4)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.renorm(input_tensor, 1, 0, 6)
print('Output tensor: ', output_tensor)