'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(10, 5, 10)
k = 2
dim = 2
largest = True
sorted = True
topk_result = torch.topk(input, k, dim, largest, sorted)
print('Top K result: ', topk_result)
print('Top K value: ', topk_result[0])
print('Top K index: ', topk_result[1])