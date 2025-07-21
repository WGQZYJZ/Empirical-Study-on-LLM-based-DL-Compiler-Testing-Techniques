'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: \n', input_tensor)
print('\nTask 3: Call the API torch.Tensor.unsqueeze')
print('torch.Tensor.unsqueeze(_input_tensor, dim)')
print('Dimension: 0')
print('Output tensor: \n', input_tensor.unsqueeze(0))
print('\nDimension: 1')
print('Output tensor: \n', input_tensor.unsqueeze(1))
print('\nDimension: 2')
print('Output tensor: \n', input_tensor.unsqueeze(2))