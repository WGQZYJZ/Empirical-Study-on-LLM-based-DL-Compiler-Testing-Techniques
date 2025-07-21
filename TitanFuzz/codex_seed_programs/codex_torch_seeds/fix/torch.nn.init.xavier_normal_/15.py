'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(10, 10))
print(input)
torch.nn.init.xavier_normal_(input)
print(input)