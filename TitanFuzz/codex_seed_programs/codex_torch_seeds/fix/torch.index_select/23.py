'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input = torch.randn(3, 4)
index = torch.tensor([0, 2])
result = torch.index_select(input, 0, index)
print('input:')
print(input)
print('index:')
print(index)
print('result:')
print(result)