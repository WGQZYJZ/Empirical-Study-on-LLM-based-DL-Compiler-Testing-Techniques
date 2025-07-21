import torch
from torch import nn
from torch.autograd import Variable
input_tensor = Variable(torch.randn(1, 1, 7, 7))
output_tensor = torch.nn.functional.unfold(input_tensor, kernel_size=3, padding=1, stride=1)