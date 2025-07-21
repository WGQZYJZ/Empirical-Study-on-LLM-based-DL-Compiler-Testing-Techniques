'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.hardshrink(0.5)
print('Output Tensor: ', output_tensor)