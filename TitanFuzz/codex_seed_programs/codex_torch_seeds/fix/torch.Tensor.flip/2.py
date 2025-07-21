'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
import numpy as np
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: \n', input_tensor)
flipped_tensor = torch.Tensor.flip(input_tensor, [0])
print('Flipped tensor: \n', flipped_tensor)