"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.binary_cross_entropy_with_logits\ntorch.nn.functional.binary_cross_entropy_with_logits(input, target, weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None)\n"
import torch
import torch.nn.functional as F
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
out = F.binary_cross_entropy_with_logits(x, y)
print(out)
print(x.grad, y.grad)