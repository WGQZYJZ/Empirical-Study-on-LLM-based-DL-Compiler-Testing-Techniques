'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
x = torch.randn(4, 5)
print(x)
topk_output = torch.topk(x, 2)
print(topk_output)
topk_output = torch.topk(x, 2, dim=1)
print(topk_output)
topk_output = torch.topk(x, 2, dim=1, largest=False)
print(topk_output)
topk_output = torch.topk(x, 2, dim=1, largest=False, sorted=False)
print(topk_output)