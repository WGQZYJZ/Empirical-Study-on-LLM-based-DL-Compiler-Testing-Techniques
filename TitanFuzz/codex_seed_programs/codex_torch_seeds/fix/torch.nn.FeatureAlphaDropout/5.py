'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.nn import FeatureAlphaDropout
import torch
input = torch.randn(1, 5)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
print(input)