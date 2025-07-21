'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(10, 10))
w = Variable(torch.randn(10, 10), requires_grad=True)
torch.nn.utils.clip_grad_norm_(w, max_norm=1.0)