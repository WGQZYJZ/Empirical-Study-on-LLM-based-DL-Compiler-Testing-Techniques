import torch
from torch import nn
from torch.autograd import Variable
data = np.random.rand(2, 3)
input_data = torch.Tensor(data)
hardtanh = torch.nn.Hardtanh()
output = hardtanh(input_data)