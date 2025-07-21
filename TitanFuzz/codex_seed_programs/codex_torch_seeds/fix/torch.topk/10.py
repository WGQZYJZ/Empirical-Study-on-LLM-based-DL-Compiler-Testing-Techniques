'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
import numpy as np
'\nimport PyTorch\n'
'\nGenerate input data\n'
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
'\nCall the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
topk_data = torch.topk(data, 2, dim=1)
for i in range(len(topk_data[0])):
    print(topk_data[0][i])
for i in range(len(topk_data[1])):
    print