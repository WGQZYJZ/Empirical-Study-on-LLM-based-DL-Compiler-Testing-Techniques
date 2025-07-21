'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
alpha_dropout = nn.AlphaDropout(p=0.5, inplace=False)
output = alpha_dropout(x)
print(output)