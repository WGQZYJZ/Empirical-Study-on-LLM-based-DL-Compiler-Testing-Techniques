import torch
from torch import nn
from torch.autograd import Variable
input_size = (8, 16, 16, 16)
input_data = torch.randn(*input_size)
start = time.time()
output = torch.fft.fftn(input_data, norm='ortho')
end = time.time()