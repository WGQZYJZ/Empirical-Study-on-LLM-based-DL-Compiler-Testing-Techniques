'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
import numpy as np
import torch
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
result = torch.topk(x, k=2, dim=1)
print(result)
print(result[0])
print(result[1])