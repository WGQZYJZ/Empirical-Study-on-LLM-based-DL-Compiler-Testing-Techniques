'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svdvals\ntorch.linalg.svdvals(A, *, out=None)\n'
import torch
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print('a: ', a)
print('torch.linalg.svdvals(a): ', torch.linalg.svdvals(a))