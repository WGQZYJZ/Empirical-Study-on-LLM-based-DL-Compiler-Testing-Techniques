'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal_\ntorch.Tensor.reciprocal_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:')
print(input_tensor)
print('\nReciprocal of input tensor:')
print(torch.Tensor.reciprocal_(input_tensor))
print('\nReciprocal of input tensor:')
print(input_tensor)