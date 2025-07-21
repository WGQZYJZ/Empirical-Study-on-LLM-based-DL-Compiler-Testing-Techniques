import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]))
output = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=1, padding=1)