'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ravel\ntorch.Tensor.ravel(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('input_tensor: ', input_tensor)
print('\nTask 3: Call the API torch.Tensor.ravel')
print('torch.Tensor.ravel(input_tensor) = ', input_tensor.ravel())