'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('input_tensor = \n', input_tensor)
print('Task 3: Call the API torch.Tensor.masked_select')
mask = torch.ByteTensor([[0, 0, 1], [1, 0, 1], [0, 1, 1]])
print('mask = \n', mask)
output_tensor = torch.Tensor.masked_select(input_tensor, mask)
print('output_tensor = \n', output_tensor)