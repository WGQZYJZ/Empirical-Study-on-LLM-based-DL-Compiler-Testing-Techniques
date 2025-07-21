import torch
from torch import nn
from torch.autograd import Variable
tensors = []
for i in range(4):
    tensors.append(torch.rand(3, 4))
result = torch.broadcast_tensors(*tensors)