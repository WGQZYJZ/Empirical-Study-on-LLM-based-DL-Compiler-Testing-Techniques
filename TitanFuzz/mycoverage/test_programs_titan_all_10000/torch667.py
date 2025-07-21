import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[[[1, 2], [3, 4]]]]))
output_data = torch.nn.functional.upsample_nearest(input_data, scale_factor=3)