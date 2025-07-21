'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SiLU\ntorch.nn.SiLU(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(5, 3))
print(x)
y = torch.nn.SiLU(inplace=False)
print(y(x))