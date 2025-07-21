'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 2)
print(input)
output = F.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
print(output)