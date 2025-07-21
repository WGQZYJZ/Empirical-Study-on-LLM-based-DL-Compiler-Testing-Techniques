'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print(input)
index = torch.tensor([1, 2, 0, 2, 1])
print(index)
output = torch.index_select(input, 1, index)
print(output)