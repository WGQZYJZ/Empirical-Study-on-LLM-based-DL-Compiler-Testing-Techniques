'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_value_\ntorch.nn.utils.clip_grad_value_(parameters, clip_value)\n'
import torch
import torch.nn as nn
import torch.optim as optim
import torch
import torch.nn as nn
import torch.optim as optim
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.nn.utils.clip_grad_value_(x, 1)
torch.nn.utils.clip_grad_value_(y, 1)
print(x.grad)
print(y.grad)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2)\n'
import torch
import torch.nn as nn
import torch.optim as optim