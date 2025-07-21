'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu_\ntorch.nn.functional.rrelu_(input, lower=1./8, upper=1./3, training=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(10, 10)
F.rrelu_(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False)
print(input)