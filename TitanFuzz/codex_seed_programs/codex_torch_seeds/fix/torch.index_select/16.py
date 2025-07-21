'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
print(torch.index_select(x, 0, torch.tensor([0, 2])))
print(torch.index_select(x, 1, torch.tensor([0, 2])))