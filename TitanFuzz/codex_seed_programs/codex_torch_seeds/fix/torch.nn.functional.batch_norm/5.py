'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.batch_norm\ntorch.nn.functional.batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(2, 3, 4, 4)
output = F.batch_norm(input, None, None, None, None, True)
print(output)