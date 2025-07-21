'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
import numpy as np
x = torch.randn(3, 5)
y = torch.randn(3, 5)
distance = nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)
output = distance(x, y)
print(output)