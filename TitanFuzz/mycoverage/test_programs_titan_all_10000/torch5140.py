import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 10, dtype=torch.float)
result = torch.hamming_window(10, periodic=True)