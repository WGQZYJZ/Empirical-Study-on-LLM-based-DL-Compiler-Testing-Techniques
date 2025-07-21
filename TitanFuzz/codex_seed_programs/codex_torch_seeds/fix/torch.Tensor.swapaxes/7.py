'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input tensor:')
print(input)
print('\n')
print('Output tensor:')
print(input.swapaxes(1, 2))