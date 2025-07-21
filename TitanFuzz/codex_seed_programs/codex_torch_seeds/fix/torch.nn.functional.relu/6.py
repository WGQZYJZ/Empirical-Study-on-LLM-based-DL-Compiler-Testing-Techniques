'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
import numpy as np
x = torch.randn(1, 3)
print(x)
y = torch.nn.functional.relu(x)
print(y)