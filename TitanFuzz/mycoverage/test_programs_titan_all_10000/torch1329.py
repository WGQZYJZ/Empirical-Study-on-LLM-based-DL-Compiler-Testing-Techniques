import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(2, 3, requires_grad=True)
output_data = torch.logit(input_data)
sigmoid_data = torch.sigmoid(output_data)
log_data = torch.log(sigmoid_data)