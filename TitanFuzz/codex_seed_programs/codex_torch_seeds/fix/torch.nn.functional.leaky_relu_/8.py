'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
print(x)
print(torch.nn.functional.leaky_relu_(x))