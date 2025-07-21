'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool1d\ntorch.nn.functional.max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
import numpy as np
x = torch.randn(1, 1, 3)
torch.nn.functional.max_pool1d(x, kernel_size=2, stride=1, padding=0)