import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(1, 4, 4)
y = torch.fft.fft(x)
x_np = x.numpy()
y_np = y.numpy()
x_np_fft = np.fft.fft(x_np)
x_np = x.numpy()
y_np = y.numpy()
x_np_fft = np.fft.fft(x_np)