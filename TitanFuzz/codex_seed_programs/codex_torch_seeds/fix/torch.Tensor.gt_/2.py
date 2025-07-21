'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt_\ntorch.Tensor.gt_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
torch.Tensor.gt_(input_tensor, torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print('Input tensor: {}'.format(input_tensor))
torch.Tensor.gt_(input_tensor, torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print('Input tensor: {}'.format(input_tensor))