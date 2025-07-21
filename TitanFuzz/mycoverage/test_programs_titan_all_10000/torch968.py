import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 10, (3, 3))
result_tensor = torch.Tensor.long(input_tensor)