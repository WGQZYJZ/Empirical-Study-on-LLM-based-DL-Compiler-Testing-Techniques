import torch
from torch import nn
from torch.autograd import Variable
in_data = np.random.randn(4, 3, 2)
in_tensor = torch.tensor(in_data)
out_tensor = torch.fft.fft(in_tensor)