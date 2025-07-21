'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input = Variable(torch.randn(1, 3))
print('input:', input)
print('\nFeatureAlphaDropout(p=0.5, inplace=False):')
feature_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=False)
print('feature_dropout:', feature_dropout)
print('feature_dropout(input):', feature_dropout(input))
print('\nFeatureAlphaDropout(p=0.5, inplace=True):')
feature_dropout = nn.FeatureAlphaDropout(p=0.5, inplace=True)
print('feature_dropout:', feature_dropout)
print('feature_dropout(input):', feature_dropout(input))