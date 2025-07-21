'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 0.5)
torch.nn.utils.clip_grad_value_(y, 0.5)
print(x.grad)
print(y.grad)