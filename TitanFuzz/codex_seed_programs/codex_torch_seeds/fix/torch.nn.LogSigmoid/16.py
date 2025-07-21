'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
from torch.autograd import Variable
import numpy as np
x = Variable(torch.randn(5, 5))
print(x)
print(torch.nn.LogSigmoid()(x))