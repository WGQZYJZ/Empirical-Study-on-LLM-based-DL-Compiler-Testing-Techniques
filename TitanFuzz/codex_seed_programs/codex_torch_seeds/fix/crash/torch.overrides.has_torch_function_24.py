'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.has_torch_function\ntorch.overrides.has_torch_function()\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.randn(2, 3)
print(torch.overrides.has_torch_function(nn.Linear(3, 4)))
print(torch.overrides.has_torch_function(nn.BatchNorm2d(3)))
print(torch.overrides.has_torch_function(nn.ReLU()))
print(torch.overrides.has_torch_function(nn.MaxPool2d(3)))