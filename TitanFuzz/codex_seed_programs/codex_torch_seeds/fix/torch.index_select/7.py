'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
tensor = torch.randn(4, 4)
print(tensor)
index = torch.LongTensor([0, 2])
print(index)
print(torch.index_select(tensor, 0, index))
print(torch.index_select(tensor, 1, index))