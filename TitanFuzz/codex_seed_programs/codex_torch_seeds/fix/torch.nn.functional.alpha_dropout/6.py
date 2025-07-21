'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(5, 5)
print('Input:', input)
output = nn.functional.alpha_dropout(input)
print('Output:', output)