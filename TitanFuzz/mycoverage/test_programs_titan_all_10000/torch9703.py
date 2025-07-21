import torch
from torch import nn
from torch.autograd import Variable
if True:
    input_tensor = torch.rand(3, 3)
    print(input_tensor)
    output_tensor = torch.Tensor.subtract(input_tensor, 0.5)
    print(output_tensor)