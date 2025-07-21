"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import numpy as np
import torch
x = torch.ones(5, 5)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
print(x)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
print(x)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
print(x)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
print(x)