'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(20, 16)
alphaDropout = nn.AlphaDropout(p=0.5)
output = alphaDropout(input)
print(output)