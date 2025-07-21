"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.poisson_nll_loss\ntorch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1)
target = torch.randn(1, 1)
output = F.poisson_nll_loss(input, target)
print(output)