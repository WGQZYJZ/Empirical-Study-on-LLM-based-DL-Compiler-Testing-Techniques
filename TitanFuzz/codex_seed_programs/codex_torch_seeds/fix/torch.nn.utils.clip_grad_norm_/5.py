'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
x = Variable(torch.randn(10, 5))
y = Variable(torch.randn(10, 5))
torch.nn.utils.clip_grad_norm_(x, max_norm=2, norm_type=2)
torch.nn.utils.clip_grad_norm_(y, max_norm=2, norm_type=2)
print(x)
print(y)