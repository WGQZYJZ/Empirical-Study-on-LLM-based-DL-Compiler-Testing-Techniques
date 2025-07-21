import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[3.0, (- 4.0)], [1.0, (- 2.0)]], requires_grad=True)
output = torch.empty(input_data.size())