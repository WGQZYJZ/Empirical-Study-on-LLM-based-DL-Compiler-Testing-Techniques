'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
other_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [0, 0, 1]], dtype=torch.bool)
print('input_tensor: \n', input_tensor)
print('other_tensor: \n', other_tensor)
result = torch.logical_and(input_tensor, other_tensor)
print('result: \n', result)