'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False, min_value=None, max_value=None)\n'
import torch
import numpy as np
import torch.nn as nn
x = torch.randn(2, 3)
print(x)
hardtanh = nn.Hardtanh(min_val=(- 1.0), max_val=1.0)
print(hardtanh(x))