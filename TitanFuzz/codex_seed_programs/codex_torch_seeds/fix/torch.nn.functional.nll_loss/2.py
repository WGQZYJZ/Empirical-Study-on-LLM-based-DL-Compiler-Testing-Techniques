"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])
print(F.nll_loss(F.log_softmax(input), target))
input = torch.randn(3, 5, requires_grad=True)
target = torch.tensor([1, 0, 4])
print(F.nll_loss(F.log_softmax(input), target, reduction='sum'))
input = torch.randn(3, 5, requires_grad=True)