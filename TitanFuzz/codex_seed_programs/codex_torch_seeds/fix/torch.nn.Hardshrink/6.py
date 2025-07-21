'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
input_data = Variable(torch.rand(5, 10))
torch.nn.Hardshrink(lambd=0.5)(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardtanh\ntorch.nn.Hardtanh(min_val=-1.0, max_val=1.0, inplace=False)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
input_data = Variable(torch.rand(5, 10))