import torch
from torch import nn
from torch.autograd import Variable
module = torch.nn.Linear(10, 10)
tensor_name = 'weight'
torch.nn.utils.parametrize.is_parametrized(module, tensor_name)