'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.parameter.UninitializedParameter\ntorch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(2, 3)
print(x)
torch.nn.parameter.UninitializedParameter(requires_grad=True, device=None, dtype=None)