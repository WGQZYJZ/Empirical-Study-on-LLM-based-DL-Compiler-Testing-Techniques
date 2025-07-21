"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SmoothL1Loss\ntorch.nn.SmoothL1Loss(size_average=None, reduce=None, reduction='mean', beta=1.0)\n"
import torch
import torch.nn as nn
import numpy as np
input = torch.Tensor(np.random.random((3, 5)))
target = torch.Tensor(np.random.random((3, 5)))
loss_fn = nn.SmoothL1Loss()
loss = loss_fn(input, target)
print(loss)