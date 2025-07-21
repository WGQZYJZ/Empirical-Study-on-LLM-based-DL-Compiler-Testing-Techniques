'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)
print('Output tensor: ', output_tensor)
print('Result tensor: ', output_tensor)