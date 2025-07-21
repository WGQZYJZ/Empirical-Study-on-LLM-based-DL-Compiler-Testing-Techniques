'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
import numpy as np
import torch
import torch.nn as nn
x = torch.randn(4, 4)
print(x)
y = nn.functional.softplus(x)
print(y)