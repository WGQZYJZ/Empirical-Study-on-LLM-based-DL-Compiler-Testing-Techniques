'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input tensor: {}'.format(input_tensor))
output_tensor = input_tensor.narrow_copy(0, 1, 2)
print('Output tensor: {}'.format(output_tensor))