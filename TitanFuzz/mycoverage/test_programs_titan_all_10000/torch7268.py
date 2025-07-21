import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
tensor3 = torch.vstack((tensor1, tensor2))