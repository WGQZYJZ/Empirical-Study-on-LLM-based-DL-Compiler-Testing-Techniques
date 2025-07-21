'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 2, 4, 2, 1, 2, 3, 2, 4, 2, 1, 2, 3, 2, 4, 2, 1, 2, 3, 2, 4, 2])
weights = torch.tensor([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print('Input tensor: {}'.format(input_tensor))
print('Weights tensor: {}'.format(weights))
print('Output tensor: {}'.format(torch.Tensor.bincount(input_tensor, weights=weights, minlength=5)))