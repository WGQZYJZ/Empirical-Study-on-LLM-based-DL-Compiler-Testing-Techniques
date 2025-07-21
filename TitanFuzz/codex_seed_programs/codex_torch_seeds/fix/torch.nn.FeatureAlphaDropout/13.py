'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FeatureAlphaDropout\ntorch.nn.FeatureAlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = torch.randn(100, 100)
x = Variable(x)
torch.nn.FeatureAlphaDropout(p=0.5, inplace=False)
F.dropout(x, p=0.5, training=True, inplace=False)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = torch.randn(100, 100)