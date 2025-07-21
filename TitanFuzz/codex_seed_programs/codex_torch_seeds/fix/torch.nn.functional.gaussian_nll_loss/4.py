"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gaussian_nll_loss\ntorch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')\n"
import torch
import torch.nn.functional as F
import torch
import torch.nn.functional as F
x = torch.randn(10, 1)
y = torch.randn(10, 1)
loss = F.gaussian_nll_loss(x, y, torch.ones(10, 1))
print(loss)