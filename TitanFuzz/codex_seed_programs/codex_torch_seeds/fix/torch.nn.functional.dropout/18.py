'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.parameter import Parameter
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.nn.init as init
from torch.nn import Linear, Conv2d, BatchNorm2d, MaxPool2d, Dropout2d, Dropout, MaxPool1d, Conv1d
from torch.nn.functional import relu, elu, relu6, sigmoid, tanh, softmax
import numpy as np
import pdb
input = torch.randn(20, 16)
output = F.dropout(input, p=0.5, training=True)
print('input: ', input)
print('output: ', output)