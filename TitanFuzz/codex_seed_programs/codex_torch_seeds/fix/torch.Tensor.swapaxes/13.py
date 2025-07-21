'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapaxes\ntorch.Tensor.swapaxes(_input_tensor, axis0, axis1)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input tensor:')
print(input_tensor)
swap_tensor = torch.Tensor.swapaxes(input_tensor, 0, 1)
print('Swap tensor:')
print(swap_tensor)