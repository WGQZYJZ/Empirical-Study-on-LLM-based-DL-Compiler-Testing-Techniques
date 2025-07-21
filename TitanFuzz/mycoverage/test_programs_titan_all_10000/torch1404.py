import torch
from torch import nn
from torch.autograd import Variable
input = np.random.rand(2, 3, 4)
input = torch.Tensor(input)
output = torch.nn.functional.tanhshrink(input)