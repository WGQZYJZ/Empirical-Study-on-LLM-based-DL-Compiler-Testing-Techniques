"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.l1_loss\ntorch.nn.functional.l1_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
output = F.l1_loss(input, target)
print(output)
output.backward()
print(input.grad)