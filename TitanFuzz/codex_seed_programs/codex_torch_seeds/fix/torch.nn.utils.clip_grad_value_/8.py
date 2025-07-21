'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch.nn as nn
import numpy as np
import torch
x = torch.randn(3, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
x.grad
x.grad
torch.nn.utils.clip_grad_norm_(x, 0.5)
x.grad
x = torch.randn(3, requires_grad=True)
torch.nn.utils.clip_grad_norm_(x, 0.5)
x.grad