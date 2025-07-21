'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sparse_coo_tensor\ntorch.sparse_coo_tensor(indices, values, size=None, *, dtype=None, device=None, requires_grad=False)\n'
import torch
indices = torch.LongTensor([[0, 0, 0, 1, 1, 1, 2, 2, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2]])
values = torch.FloatTensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
print('Task 1:')
print('PyTorch version: ', torch.__version__)
print('Task 2:')
print('indices: ', indices)
print('values: ', values)
print('Task 3:')
print('torch.sparse_coo_tensor(indices, values): ', torch.sparse_coo_tensor(indices, values))