'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input = torch.randn(10, 3)
index = torch.randint(low=0, high=3, size=(10,))
output = torch.index_select(input, dim=1, index=index)
print(output)