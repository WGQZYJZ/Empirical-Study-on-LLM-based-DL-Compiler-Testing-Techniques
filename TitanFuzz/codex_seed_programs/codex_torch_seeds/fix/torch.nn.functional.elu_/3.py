'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
import torch.nn as nn
input = torch.randn(3, 5)
output = nn.functional.elu_(input)
print(input)
print(output)
elu = nn.ELU(alpha=1.0, inplace=False)
output = elu(input)
print(output)