import torch
from torch import nn
from torch.autograd import Variable

tensor1 = torch.rand(4, 4)
tensor2 = torch.rand(4, 4)
tensor3 = torch.rand(4, 4)
tensor4 = torch.addcmul(tensor1, tensor2, tensor3)