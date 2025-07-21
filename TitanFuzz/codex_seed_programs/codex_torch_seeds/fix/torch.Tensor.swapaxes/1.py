'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print('Input Tensor:')
print(input_tensor)
swapped_tensor = input_tensor.swapaxes(0, 1)
print('Swapped Tensor:')
print(swapped_tensor)
'\nTask 4: Call the API torch.Tensor.transpose\ntorch.Tensor.transpose(_input_tensor, dim0, dim1)\n'
transposed_tensor = input_tensor.transpose(0, 1)
print('Transposed Tensor:')
print(transposed_tensor)