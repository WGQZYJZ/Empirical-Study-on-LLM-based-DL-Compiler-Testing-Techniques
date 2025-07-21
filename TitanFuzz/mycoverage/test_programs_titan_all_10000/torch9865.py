import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(1, 3, 224, 224)
torch.Tensor.is_set_to(input_tensor, input_tensor)