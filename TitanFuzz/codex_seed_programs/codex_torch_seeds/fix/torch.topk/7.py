'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
data = torch.tensor([[1, 3, 5], [2, 4, 6], [3, 5, 7]])
print('data: ', data)
print('k = 1: ', torch.topk(data, 1))
print('k = 2: ', torch.topk(data, 2))
print('k = 3: ', torch.topk(data, 3))
print('k = 1, dim = 0: ', torch.topk(data, 1, dim=0))
print('k = 2, dim = 0: ', torch.topk(data, 2, dim=0))
print('k = 3, dim = 0: ', torch.topk(data, 3, dim=0))