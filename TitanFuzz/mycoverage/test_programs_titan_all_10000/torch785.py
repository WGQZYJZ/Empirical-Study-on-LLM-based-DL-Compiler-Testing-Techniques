import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(2, 3, 4, 5)
input_data = torch.tensor(input_data)
output = torch.fft.fft2(input_data)
output = torch.fft.ifft2(input_data)
output = torch.fft.rfft2(input_data)
output = torch.fft.irfft2(input_data)