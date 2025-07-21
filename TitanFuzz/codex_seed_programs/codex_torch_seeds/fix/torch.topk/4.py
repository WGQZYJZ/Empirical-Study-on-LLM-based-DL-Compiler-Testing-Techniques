'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.topk\ntorch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)\n'
import torch
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print(input)
k = 1
dim = 0
largest = True
sorted = True
(output, indices) = torch.topk(input, k, dim, largest, sorted)
print(output)
print(indices)
k = 1
dim = 0
largest = True
sorted = False
(output, indices) = torch.topk(input, k, dim, largest, sorted)
print(output)
print(indices)
k = 1
dim = 1
largest = True
sorted = True
(output, indices) = torch.topk(input, k, dim, largest, sorted)
print