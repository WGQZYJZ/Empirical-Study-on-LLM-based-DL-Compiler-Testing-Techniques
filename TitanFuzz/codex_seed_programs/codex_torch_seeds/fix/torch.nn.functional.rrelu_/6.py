'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu_\ntorch.nn.functional.rrelu_(input, lower=1./8, upper=1./3, training=False)\n'
import torch
import numpy as np
input = torch.randn(5, 5)
torch.nn.functional.rrelu_(input)
print(input)