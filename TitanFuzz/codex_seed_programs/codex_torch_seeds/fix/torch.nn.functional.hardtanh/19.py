'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1., max_val=1., inplace=False)\n'
import torch
import numpy as np
import torch
x = torch.randn(4, 3)
x_hat = torch.nn.functional.hardtanh(x, min_val=(- 1.0), max_val=1.0, inplace=False)
print(x_hat)
print(x_hat.shape)
print(x_hat.shape)
print(x_hat.shape)
print(x_hat.shape)