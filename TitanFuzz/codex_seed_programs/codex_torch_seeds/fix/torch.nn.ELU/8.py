'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
x = torch.randn(1, 1, 3, 3)
m = nn.ELU(alpha=1.0, inplace=False)
print(m(x))