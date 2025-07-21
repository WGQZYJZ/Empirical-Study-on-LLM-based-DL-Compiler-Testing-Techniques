"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PoissonNLLLoss\ntorch.nn.PoissonNLLLoss(log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
n = 1
input = torch.randn(n, 1)
target = torch.randn(n, 1)
loss = nn.PoissonNLLLoss(reduction='sum')
output = loss(input, target)
print(output)