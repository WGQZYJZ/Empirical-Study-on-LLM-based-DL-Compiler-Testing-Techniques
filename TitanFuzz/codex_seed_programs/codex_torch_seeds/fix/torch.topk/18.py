'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print(x)
print(torch.topk(x, 2))
print(torch.topk(x, 2, dim=1))
print(torch.topk(x, 2, dim=1, largest=False))
print(torch.topk(x, 3, dim=0, largest=True, sorted=False))
print(torch.topk(x, 3, dim=1, largest=True, sorted=False)[0])