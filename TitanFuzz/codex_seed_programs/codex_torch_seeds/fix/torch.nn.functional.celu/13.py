'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
import torch.nn as nn
input = torch.randn(1, 3, 3, 3)
print(input)
import torch
import torch.nn as nn
input = torch.randn(1, 3, 3, 3)
print(input)
output = nn.functional.celu(input)
print(output)
output = nn.functional.celu(input, alpha=0.5)
print(output)
output = nn.functional.celu(input, alpha=0.5, inplace=True)
print(output)