'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expand_as\ntorch.Tensor.expand_as(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Tensor: \n', input_tensor)
other_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Other Tensor: \n', other_tensor)
expanded_tensor = input_tensor.expand_as(other_tensor)
print('Expanded Tensor: \n', expanded_tensor)