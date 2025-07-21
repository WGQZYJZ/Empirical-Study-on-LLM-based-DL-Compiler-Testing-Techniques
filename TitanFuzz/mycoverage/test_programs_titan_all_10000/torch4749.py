import torch
from torch import nn
from torch.autograd import Variable
dividend = torch.randn(2, 3)
divisor = torch.randn(2, 3)
true_divide = torch.true_divide(dividend, divisor)