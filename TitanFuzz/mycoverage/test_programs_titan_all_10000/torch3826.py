import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]], [[21, 22, 23], [24, 25, 26], [27, 28, 29]]])
output_tensor_list = torch.Tensor.dsplit(input_tensor, 3)