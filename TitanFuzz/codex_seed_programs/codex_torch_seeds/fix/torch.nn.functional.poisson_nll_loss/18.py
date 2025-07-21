"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.poisson_nll_loss\ntorch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.rand(1, 1, 5, 5)
target = torch.rand(1, 1, 5, 5)
loss = torch.nn.functional.poisson_nll_loss(input, target)
print(loss)