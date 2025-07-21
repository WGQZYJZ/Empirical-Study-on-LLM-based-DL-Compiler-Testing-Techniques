'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
import numpy as np
import torch
x = torch.linspace(0, 1, steps=5)
y = torch.linspace(0, 1, steps=5)
(xv, yv) = torch.meshgrid([x, y])
print('xv:', xv)
print('yv:', yv)
print('xv.shape:', xv.shape)
print('yv.shape:', yv.shape)
print('xv.size():', xv.size())
print('yv.size():', yv.size())
print('xv.dtype:', xv.dtype)
print('yv.dtype:', yv.dtype)
print('xv.device:', xv.device)
print('yv.device:', yv.device)
print('xv.requires_grad:', xv.requires_grad)