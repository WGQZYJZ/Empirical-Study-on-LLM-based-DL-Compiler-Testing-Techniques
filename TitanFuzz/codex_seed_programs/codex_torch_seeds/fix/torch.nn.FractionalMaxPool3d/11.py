'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
from torch.autograd import Variable
from torch.nn.parameter import Parameter
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.nn.init as init
import torch
input = Variable(torch.randn(20, 16, 50, 32, 45))
pool = nn.FractionalMaxPool3d(kernel_size=(3, 2, 2), output_size=(5, 6, 7))
output = pool(input)
print(output.shape)