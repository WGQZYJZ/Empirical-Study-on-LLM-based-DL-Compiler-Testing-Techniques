'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 3, 3)
output = F.rrelu(input)
print(output)