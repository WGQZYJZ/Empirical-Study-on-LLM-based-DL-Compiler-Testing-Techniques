"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PoissonNLLLoss\ntorch.nn.PoissonNLLLoss(log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import numpy as np
print('PyTorch version:', torch.__version__)
input_data = torch.rand(10, 5)
target = torch.randint(5, size=(10, 1))
loss_fn = nn.PoissonNLLLoss()
output = loss_fn(input_data, target)
print('output:', output)