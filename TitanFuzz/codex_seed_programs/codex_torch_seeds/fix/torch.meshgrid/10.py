'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.meshgrid\ntorch.meshgrid(*tensors)\n'
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable
import numpy as np
x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))
print(torch.meshgrid([torch.arange(0, 2), torch.arange(0, 3)])[0])
print(torch.meshgrid([torch.arange(0, 2), torch.arange(0, 3)])[1])