import torch
from torch import nn
from torch.autograd import Variable
input1 = torch.tensor([1, 2, 3])
input2 = torch.tensor([1, 2, 3], dtype=torch.float32)
input3 = torch.tensor([1, 2, 3], dtype=torch.float64)
input4 = torch.tensor([1, 2, 3], dtype=torch.complex64)
output1 = torch.isreal(input1)
output2 = torch.isreal(input2)
output3 = torch.isreal(input3)
output4 = torch.isreal(input4)