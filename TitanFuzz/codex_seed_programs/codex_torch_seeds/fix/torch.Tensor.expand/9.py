'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand\ntorch.Tensor.expand(_input_tensor, *sizes)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: {}'.format(torch.__version__))
print('\nTask 2: Generate input data')
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: {}'.format(input_tensor))
print('\nTask 3: Call the API torch.Tensor.expand')
output_tensor = input_tensor.expand(2, 3, 4)
print('Output tensor: {}'.format(output_tensor))