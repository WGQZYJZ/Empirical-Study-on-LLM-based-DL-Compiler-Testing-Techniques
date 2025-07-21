'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
x = Variable(torch.randn(1, 1, 4, 4))
feature_alpha_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
print(feature_alpha_dropout(x))