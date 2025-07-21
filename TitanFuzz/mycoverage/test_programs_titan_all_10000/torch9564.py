import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- 0.0), (- 1.0), 0.0, 1.0, 2.0, float('inf'), float('nan'), float('-inf')])
result = torch.Tensor.isneginf(input_tensor)