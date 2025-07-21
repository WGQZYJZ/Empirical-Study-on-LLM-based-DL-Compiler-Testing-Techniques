'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print(a)
(top_k_value, top_k_idx) = torch.topk(a, 2)
print(top_k_value)
print(top_k_idx)