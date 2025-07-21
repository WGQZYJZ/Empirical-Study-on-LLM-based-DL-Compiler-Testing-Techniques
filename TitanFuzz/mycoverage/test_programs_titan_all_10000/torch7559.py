import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(4, 4, 4)
y = torch.fft.rfftn(x)
x_np = x.numpy()
y_np = y.numpy()
y_np_verify = np.fft.rfftn(x_np)