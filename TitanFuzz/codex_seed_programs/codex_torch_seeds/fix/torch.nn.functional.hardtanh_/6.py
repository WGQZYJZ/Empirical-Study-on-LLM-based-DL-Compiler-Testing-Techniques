'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh_\ntorch.nn.functional.hardtanh_(input, min_val=-1., max_val=1.)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
print(input)
print(torch.nn.functional.hardtanh_(input))