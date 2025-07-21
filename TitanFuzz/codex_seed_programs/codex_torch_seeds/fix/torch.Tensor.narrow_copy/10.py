'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow_copy\ntorch.Tensor.narrow_copy(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.arange(1, 17).view(4, 4)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', input_tensor.narrow_copy(0, 0, 2))