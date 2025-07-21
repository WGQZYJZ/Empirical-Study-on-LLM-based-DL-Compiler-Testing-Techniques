'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_quantized\ntorch.Tensor.is_quantized(_input_tensor, )\n'
import torch
import numpy as np
import torch
input_tensor = torch.rand(1, 1, 2, 2)
torch.Tensor.is_quantized(input_tensor)
print('The input tensor is quantized: ', torch.Tensor.is_quantized(input_tensor))