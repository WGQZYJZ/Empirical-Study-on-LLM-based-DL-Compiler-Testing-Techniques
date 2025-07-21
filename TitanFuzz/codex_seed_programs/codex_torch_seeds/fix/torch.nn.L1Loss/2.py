"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.L1Loss\ntorch.nn.L1Loss(size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch.nn as nn
import numpy as np
import torch
from torch.autograd import Variable
import torch.nn as nn
import numpy as np
x_input = Variable(torch.randn(2, 3))
y_input = Variable(torch.randn(2, 3))
loss = nn.L1Loss()
loss(x_input, y_input)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
from torch.autograd import Variable
import torch.nn as nn
import numpy as np
import torch
from torch.autograd import Variable