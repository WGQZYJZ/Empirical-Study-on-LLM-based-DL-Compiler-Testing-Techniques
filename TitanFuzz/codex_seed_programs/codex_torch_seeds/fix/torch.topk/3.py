'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('input data: ', input)
k = 2
(value, index) = torch.topk(input, k)
print('value: ', value)
print('index: ', index)