import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.rand(2, 3)
tensor2 = torch.rand(2, 3)
result = torch.result_type(tensor1, tensor2)