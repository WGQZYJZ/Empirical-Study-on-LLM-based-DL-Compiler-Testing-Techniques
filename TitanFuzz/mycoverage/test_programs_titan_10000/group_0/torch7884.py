import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(1, 2, 3, 4)
start = time.time()
output = torch.fft.fftn(input)
end = time.time()