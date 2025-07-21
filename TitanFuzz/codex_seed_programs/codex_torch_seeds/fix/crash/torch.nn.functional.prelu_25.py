'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input = torch.randn(2, 3, 4)
weight = torch.randn(1, 3, 1)
output = F.prelu(input, weight)
print(output)