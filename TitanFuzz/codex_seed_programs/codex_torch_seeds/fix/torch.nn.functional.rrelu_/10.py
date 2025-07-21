'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu_\ntorch.nn.functional.rrelu_(input, lower=1./8, upper=1./3, training=False)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 5, 5)
torch.nn.functional.rrelu_(input)
print(input)
torch.nn.functional.rrelu_(input, training=True)
print(input)
torch.nn.functional.rrelu_(input, lower=0.4, upper=0.6)
print(input)