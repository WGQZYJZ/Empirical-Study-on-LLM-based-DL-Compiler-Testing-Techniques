'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pairwise_distance\ntorch.nn.functional.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
x1 = torch.rand(100, 128)
x2 = torch.rand(100, 128)
dist = F.pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False)
print(dist)