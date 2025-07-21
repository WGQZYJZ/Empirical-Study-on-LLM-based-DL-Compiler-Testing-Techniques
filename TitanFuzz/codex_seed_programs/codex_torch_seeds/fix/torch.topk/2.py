'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
torch.topk(a, k=2, dim=0)
torch.topk(a, k=2, dim=1)
torch.topk(a, k=2, dim=0, largest=False)
torch.topk(a, k=2, dim=1, largest=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique\ntorch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)\n'
import torch
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)