'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input = torch.arange(0, 12).reshape(3, 4)
print(input)
index = torch.LongTensor([0, 2])
output = torch.index_select(input, 0, index)
print(output)