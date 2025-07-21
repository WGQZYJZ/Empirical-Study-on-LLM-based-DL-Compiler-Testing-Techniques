'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
print(input)
output = torch.index_select(input, 1, torch.LongTensor([0, 2]))
print(output)