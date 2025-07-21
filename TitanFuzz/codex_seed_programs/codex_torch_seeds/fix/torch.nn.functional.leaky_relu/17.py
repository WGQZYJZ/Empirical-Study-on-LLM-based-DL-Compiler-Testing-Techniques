'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
x = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
y = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=False)
torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=True)