'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.Tensor([1, 2, 3, 4, 5, 6, 6, 6])
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.bincount(input_tensor)
print('output_tensor: ', output_tensor)
output_tensor = torch.Tensor.bincount(input_tensor, weights=input_tensor)
print('output_tensor: ', output_tensor)