'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad3d\ntorch.nn.ReflectionPad3d(padding)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.ones(1, 1, 3, 3, 3))
pad = torch.nn.ReflectionPad3d(1)
print(pad(x))