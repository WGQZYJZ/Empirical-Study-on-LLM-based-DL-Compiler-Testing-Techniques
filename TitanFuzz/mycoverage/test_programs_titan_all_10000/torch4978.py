import torch
from torch import nn
from torch.autograd import Variable
input_tensor1 = torch.randn(3, 4, 5)
input_tensor2 = torch.randn(4, 5)
result = torch.broadcast_tensors(input_tensor1, input_tensor2)