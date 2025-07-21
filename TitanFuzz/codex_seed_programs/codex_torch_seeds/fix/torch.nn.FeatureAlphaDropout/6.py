'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.nn import FeatureAlphaDropout
x = torch.randn(2, 3)
print(x)
dropout = FeatureAlphaDropout(p=0.5, inplace=False)
print(dropout(x))