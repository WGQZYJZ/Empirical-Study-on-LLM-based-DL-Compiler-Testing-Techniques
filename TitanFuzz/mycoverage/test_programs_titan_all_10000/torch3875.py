import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(3, 4)
result = torch.result_type(tensor1, tensor2)