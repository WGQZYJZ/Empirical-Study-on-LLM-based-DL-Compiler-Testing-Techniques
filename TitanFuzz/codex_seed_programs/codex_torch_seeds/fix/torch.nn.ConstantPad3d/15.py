'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch.nn as nn
input = torch.ones(1, 1, 3, 3, 3)
print(input)
pad = nn.ConstantPad3d(padding=2, value=0)
print(pad(input))