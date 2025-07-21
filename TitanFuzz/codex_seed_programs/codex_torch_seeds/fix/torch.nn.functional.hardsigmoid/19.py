'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
print(x)
y = torch.nn.functional.hardsigmoid(x)
print(y)