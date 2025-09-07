import torch
from torch import nn
from torch.autograd import Variable

input_data = Variable(torch.Tensor([[(- 0.5), (- 0.5), 0.5, 0.5]]))
threshold = 0.1
threshold_layer = torch.nn.Threshold(threshold, 0)
output = threshold_layer(input_data)