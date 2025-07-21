"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gaussian_nll_loss\ntorch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input = torch.rand(3, 2)
print('input:', input)
target = torch.ones(3, 2)
print('target:', target)
var = (torch.ones(3, 2) * 0.5)
print('var:', var)
loss = F.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')
print('loss:', loss)