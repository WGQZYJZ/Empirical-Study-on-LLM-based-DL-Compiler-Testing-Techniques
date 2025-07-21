import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 10, 10, 10))
output = torch.nn.functional.local_response_norm(input_data, size=2)