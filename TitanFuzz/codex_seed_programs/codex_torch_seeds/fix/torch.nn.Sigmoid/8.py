'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sigmoid\ntorch.nn.Sigmoid()\n'
import torch
import numpy as np
x = torch.tensor([(- 1.0), 1.0, 2.0])
print(x)
y = torch.nn.Sigmoid()(x)
print(y)