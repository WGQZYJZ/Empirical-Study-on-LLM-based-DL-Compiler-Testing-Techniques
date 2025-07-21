'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReflectionPad3d\ntorch.nn.ReflectionPad3d(padding)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
input = Variable(torch.randn(1, 1, 3, 3, 3))
reflection_pad = nn.ReflectionPad3d(1)
output = reflection_pad(input)
print(output.size())