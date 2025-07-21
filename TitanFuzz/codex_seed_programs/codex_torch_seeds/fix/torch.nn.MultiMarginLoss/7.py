"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MultiMarginLoss\ntorch.nn.MultiMarginLoss(p=1, margin=1.0, weight=None, size_average=None, reduce=None, reduction='mean')\n"
import torch
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
loss = torch.nn.MultiMarginLoss()
output = loss(input, target)
print(output)
loss = torch.nn.MultiMarginLoss(p=2, margin=2.0)
output = loss(input, target)
print(output)
loss = torch.nn.MultiMarginLoss(p=2, margin=2.0, weight=torch.Tensor([1, 0.5, 0.2]))
output = loss(input, target)
print(output)