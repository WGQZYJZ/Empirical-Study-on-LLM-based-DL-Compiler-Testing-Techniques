'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
index = torch.tensor([0, 2])
print(index)
output = torch.index_select(input, dim=0, index=index)
print(output)
output = torch.index_select(input, dim=1, index=index)
print(output)