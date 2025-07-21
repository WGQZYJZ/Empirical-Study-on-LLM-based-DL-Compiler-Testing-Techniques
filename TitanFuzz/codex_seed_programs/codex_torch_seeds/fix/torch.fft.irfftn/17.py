'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
from torch.autograd import Variable
input = torch.randn(4, 4, 4)
input = Variable(input, requires_grad=True)
output = torch.fft.irfftn(input)
print(output)
output.backward(torch.randn(output.size()))
print(input.grad)