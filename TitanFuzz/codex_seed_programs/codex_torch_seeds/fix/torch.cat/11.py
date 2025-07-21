'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
t1 = torch.tensor([[1, 2], [3, 4]])
t2 = torch.tensor([[5, 6], [7, 8]])
print(torch.cat((t1, t2), dim=0))
print(torch.cat((t1, t2), dim=1))