'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.Tensor([[0.3, 0.6, 0.1], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1]])
output_tensor = input_tensor.bincount(minlength=4)
print('Output tensor: ', output_tensor)