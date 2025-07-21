'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
import torch
x = torch.ones(2, 2, requires_grad=True)
torch.nn.init.constant_(x, val=2.0)
print(x)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(input, out=None) → Tensor\n'
import torch
import torch
x = torch.ones(2, 2, requires_grad=True)
torch.nn.init.eye_(x)
print(x)