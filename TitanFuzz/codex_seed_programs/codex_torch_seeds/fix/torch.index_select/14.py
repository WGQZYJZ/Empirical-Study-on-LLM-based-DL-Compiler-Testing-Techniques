'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
index = torch.tensor([0, 2], dtype=torch.int64)
output = torch.index_select(input, 1, index)
print(output)