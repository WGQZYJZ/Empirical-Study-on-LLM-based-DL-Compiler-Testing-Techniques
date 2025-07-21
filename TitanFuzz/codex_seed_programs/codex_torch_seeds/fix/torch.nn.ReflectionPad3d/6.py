'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad3d\ntorch.nn.ReflectionPad3d(padding)\n'
import torch
import torch.nn as nn
print('PyTorch version:', torch.__version__)
input = torch.randn(1, 1, 3, 3, 3)
print('input:', input)
pad = nn.ReflectionPad3d(padding=1)
output = pad(input)
print('output:', output)