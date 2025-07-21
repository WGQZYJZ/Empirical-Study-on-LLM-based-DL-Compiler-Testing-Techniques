"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.cross_entropy\ntorch.nn.functional.cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
print('Task 3: Call the API torch.nn.functional.cross_entropy')
output = F.cross_entropy(input, target)
print(output)
print('Task 4: Call the API torch.nn.functional.cross_entropy with weight')
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
weight = torch.tensor([0.1, 1, 2, 3, 4], dtype=torch.float)
output = F.cross_entropy(input, target, weight)
print(output)