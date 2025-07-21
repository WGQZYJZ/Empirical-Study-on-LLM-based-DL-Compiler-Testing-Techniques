'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PairwiseDistance\ntorch.nn.PairwiseDistance(p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import numpy as np
import random
import torch
data = torch.randn(5, 3, requires_grad=True)
result = torch.nn.PairwiseDistance()(data, data)
print(result)