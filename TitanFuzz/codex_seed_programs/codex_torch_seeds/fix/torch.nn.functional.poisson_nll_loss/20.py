"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.poisson_nll_loss\ntorch.nn.functional.poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3))
print('input:', input)
target = Variable(torch.randn(1, 3))
print('target:', target)
output = torch.nn.functional.poisson_nll_loss(input, target)
print('output:', output)