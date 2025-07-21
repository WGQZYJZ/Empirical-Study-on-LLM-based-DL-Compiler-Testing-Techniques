'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.randn(10)
torch.nn.functional.leaky_relu_(x)
torch.nn.functional.leaky_relu_(x, negative_slope=0.5)
torch.nn.functional.leaky_relu_(x, negative_slope=1)
torch.nn.functional.leaky_relu_(x, negative_slope=2)