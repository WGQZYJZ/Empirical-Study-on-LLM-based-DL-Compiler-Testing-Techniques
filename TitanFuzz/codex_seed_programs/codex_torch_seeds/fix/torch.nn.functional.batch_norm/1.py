'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.batch_norm\ntorch.nn.functional.batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(20, 5, 10, 10)
running_mean = torch.randn(5)
running_var = torch.randn(5)
output = F.batch_norm(input, running_mean, running_var)
print('output.shape:', output.shape)