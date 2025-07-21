'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.fftshift\ntorch.fft.fftshift(input, dim=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = torch.randn(1, 5, 5)
x = Variable(x)
y = torch.fft.fftshift(x)
print(y)