import torch
from torch import nn
from torch.autograd import Variable
inputs = [torch.randn(1, 3, 224, 224), torch.randn(1, 3, 224, 224)]
shapes = torch.broadcast_shapes(*[i.shape for i in inputs])