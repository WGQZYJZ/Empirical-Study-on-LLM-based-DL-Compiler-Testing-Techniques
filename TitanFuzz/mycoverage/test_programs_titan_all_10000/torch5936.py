import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, 4, 5)
output = torch.fft.irfft2(input_data)
np_input_data = input_data.numpy()
np_output = np.fft.irfft2(np_input_data)
torch_input_data = torch.tensor(np_input_data)
torch_output = torch.fft.irfft2(torch_input_data)