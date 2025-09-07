import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[float('nan'), float('-inf'), float('inf')], [float('nan'), float('-inf'), float('inf')], [float('nan'), float('-inf'), float('inf')]])
y = torch.nan_to_num(x)