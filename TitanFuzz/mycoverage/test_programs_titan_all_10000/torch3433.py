import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]]))
input_data = Variable(torch.Tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]]))
selu_activation_function = torch.nn.SELU()
output = selu_activation_function(input_data)