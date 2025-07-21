'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor: \n', input_tensor)
output_tensor = input_tensor.hardshrink(lambd=0.5)
print('Output tensor: \n', output_tensor)