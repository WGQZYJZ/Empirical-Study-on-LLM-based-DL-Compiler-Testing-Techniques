'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.batch_norm\ntorch.nn.functional.batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1, eps=1e-05)\n'
import torch
import torch.nn as nn
x = torch.randn(4, 3, 32, 32)
y = nn.functional.batch_norm(x, None, None, None, None, True, 0.1, 1e-05)
print(y)