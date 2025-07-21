'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.count_nonzero\ntorch.count_nonzero(input, dim=None)\n'
import torch
import torch
x = torch.tensor([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
print('Number of non-zero elements in x: ', torch.count_nonzero(x))
print('Number of non-zero elements in x: ', torch.count_nonzero(x, dim=0))
print('Number of non-zero elements in x: ', torch.count_nonzero(x, dim=1))
print('Indices of non-zero elements in x: ', torch.nonzero(x))
print('Indices of non-zero elements in x: ', torch.nonzero(x, as_tuple=True))
print('Indices of non-zero elements in x: ', torch.where((x != 0)))