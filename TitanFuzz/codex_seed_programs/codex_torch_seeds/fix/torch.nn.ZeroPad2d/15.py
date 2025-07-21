'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
import numpy as np
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 4, 4))
padding = (1, 1, 1, 1)
output = torch.nn.ZeroPad2d(padding)(input)
print('input: ', input)
print('output: ', output)