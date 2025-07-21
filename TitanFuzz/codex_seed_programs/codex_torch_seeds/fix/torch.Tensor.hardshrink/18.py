'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hardshrink\ntorch.Tensor.hardshrink(_input_tensor, lambd=0.5)\n'
import torch
import torch
input_tensor = torch.rand(4, 4)
print('Input Tensor:')
print(input_tensor)
output_tensor = input_tensor.hardshrink(0.5)
print('Output Tensor:')
print(output_tensor)