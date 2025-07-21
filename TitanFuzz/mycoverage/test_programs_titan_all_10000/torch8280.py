import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.rand(3, 2)
tensor2 = torch.rand(2, 2)
tensor_row_stack = torch.row_stack((tensor1, tensor2))