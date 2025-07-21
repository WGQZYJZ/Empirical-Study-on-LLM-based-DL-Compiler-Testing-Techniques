"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.randn(3, 5, requires_grad=True)
target = torch.LongTensor(3).random_(5)
loss = torch.nn.functional.nll_loss(input, target)
print(loss)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.nll_loss\ntorch.nn.functional.nll_loss(input, target, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.randn(3, 5, requires_grad=True)
target = torch.LongTensor(3).random_(5)