'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, *, sparse_grad=False, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
print('Task 3: Call the API torch.gather')
output = torch.gather(input, 1, torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.int64))
print('output=', output)
output = torch.gather(input, 0, torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.int64))
print('output=', output)