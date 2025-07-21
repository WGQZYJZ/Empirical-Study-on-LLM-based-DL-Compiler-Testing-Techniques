import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=np.float32)
input_data = input_data.reshape((1, 1, 8))
input_data = Variable(torch.from_numpy(input_data))
result = torch.fft.rfft(input_data, n=8, dim=2, norm=None)