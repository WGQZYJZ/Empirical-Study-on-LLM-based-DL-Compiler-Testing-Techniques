'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(2, 3))
torch.nn.init.constant_(x, 2)
print(x)
print(x)
print(x.data)
print(x.data.numpy())