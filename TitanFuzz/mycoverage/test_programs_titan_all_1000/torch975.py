import torch
from torch import nn
from torch.autograd import Variable
inputData = torch.tensor([0.1, 0.5, 0.7, 1.2, (- 0.1), (- 0.5), (- 0.7), (- 1.2)])
ceilData = torch.ceil(inputData)