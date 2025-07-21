"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(3, 3, requires_grad=True)
module = nn.Linear(3, 3)
module = torch.nn.utils.weight_norm(module, name='weight', dim=0)
output = module(input)
print(output)