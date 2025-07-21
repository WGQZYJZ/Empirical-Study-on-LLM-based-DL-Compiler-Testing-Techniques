'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(4, 5)
print('Input tensor: ', input_tensor)
print('Output tensor: ', input_tensor.narrow(1, 2, 3))