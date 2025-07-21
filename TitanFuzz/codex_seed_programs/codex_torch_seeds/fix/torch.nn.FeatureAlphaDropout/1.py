'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
input = Variable(torch.randn(20, 16))
dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
output = dropout(input)
print(output)