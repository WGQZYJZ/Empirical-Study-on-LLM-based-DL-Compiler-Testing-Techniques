import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.0, (- 1.0)], [1.0, (- 1.0)]], requires_grad=True)
sigmoid = torch.nn.SiLU()
output = sigmoid(input_data)