import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
tensor3 = torch.randn(2, 3)
tensor_cat = torch.cat((tensor1, tensor2, tensor3), dim=0)