'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
import torch
input = torch.randn(20, 5)
m = torch.nn.AlphaDropout(p=0.5, inplace=False)
m = torch.nn.AlphaDropout(p=0.5, inplace=True)
output = m(input)
print(input)
print(output)