"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, dtype=torch.long).random_(5)
print(F.nll_loss(F.log_softmax(input, dim=1), target))
print(F.cross_entropy(input, target))
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)
print(F.binary_cross_entropy(F.sigmoid(input), target))
input = torch.randn(3, requires_grad=True)
target = torch.empty(3).random_(2)