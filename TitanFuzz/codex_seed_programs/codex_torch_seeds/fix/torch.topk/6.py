'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
out = torch.topk(x, 2)
print(out)
out = torch.topk(x, k=2, dim=0)
print(out)
out = torch.topk(x, k=2, dim=1)
print(out)
out = torch.topk(x, k=2, dim=1, largest=False)
print(out)