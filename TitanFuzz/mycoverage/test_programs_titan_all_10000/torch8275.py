import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
output_data = torch.nn.functional.feature_alpha_dropout(input_data, p=0.5, training=False, inplace=False)