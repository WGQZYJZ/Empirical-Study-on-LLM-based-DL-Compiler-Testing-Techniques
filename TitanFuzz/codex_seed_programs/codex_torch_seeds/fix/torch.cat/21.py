'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.rand(2, 3)
y = torch.rand(2, 3)
z = torch.rand(2, 3)
print(torch.cat((x, y, z)))
print(torch.cat((x, y, z), 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.chunk\ntorch.chunk(tensor, chunks, dim=0)\n'
import torch
x = torch.randn(4, 4)
print(torch.chunk(x, 2, 0))
print(torch.chunk(x, 2, 1))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gather\ntorch.gather(input, dim, index, out=None)\n'