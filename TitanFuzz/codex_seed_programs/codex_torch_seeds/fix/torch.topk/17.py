'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
import torch
input = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [8, 7, 6, 5]])
(topk_values, topk_indices) = torch.topk(input, k=2, dim=1)
print(topk_values)
print(topk_indices)