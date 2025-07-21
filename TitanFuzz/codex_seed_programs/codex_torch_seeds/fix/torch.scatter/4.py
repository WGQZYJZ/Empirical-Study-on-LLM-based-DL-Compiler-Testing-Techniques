'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.scatter\ntorch.scatter(input, dim, index, src)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
data = torch.tensor([[0, 1, 2], [3, 4, 5]])
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Task 3: Call the API torch.scatter')
result = torch.scatter(data, 0, index, src)
print('result: ', result)