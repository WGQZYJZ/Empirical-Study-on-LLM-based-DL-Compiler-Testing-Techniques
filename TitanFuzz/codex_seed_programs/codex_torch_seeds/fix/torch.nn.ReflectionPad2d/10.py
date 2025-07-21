'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad2d\ntorch.nn.ReflectionPad2d(padding)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch
import torch.nn as nn
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 3, 3))
m = nn.ReflectionPad2d(1)
print(m(input))
m = nn.ReflectionPad2d((1, 1, 2, 2))
print(m(input))