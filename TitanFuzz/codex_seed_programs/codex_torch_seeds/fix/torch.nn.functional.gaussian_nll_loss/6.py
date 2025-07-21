"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gaussian_nll_loss\ntorch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')\n"
import torch
import torch.nn.functional as F
input = torch.randn(3, requires_grad=True)
target = torch.randn(3)
var = torch.randn(1)
loss = F.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')
print(loss)