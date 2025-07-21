'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
x = torch.tensor([(- 1.0), 0.0, 1.0])
y = nn.Softshrink(lambd=0.5)(x)
print(y)