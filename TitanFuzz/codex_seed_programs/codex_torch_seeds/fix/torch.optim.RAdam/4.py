'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.nn as nn
from torch.optim import RAdam
from torch.optim.optimizer import Optimizer
from torch.optim.lr_scheduler import _LRScheduler
from torch.optim.lr_scheduler import ReduceLROnPlateau
input_data = torch.randn(1, 1, requires_grad=True)
target_data = torch.randn(1, 1)
optimizer = RAdam([input_data], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.step()
optimizer.zero_grad()
state_dict = optimizer.state_dict()