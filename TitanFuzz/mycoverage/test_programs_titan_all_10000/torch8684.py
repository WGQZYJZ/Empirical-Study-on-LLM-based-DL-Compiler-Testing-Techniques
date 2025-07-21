import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(1, 11)
repeated_data = torch.repeat_interleave(data, repeats=3)