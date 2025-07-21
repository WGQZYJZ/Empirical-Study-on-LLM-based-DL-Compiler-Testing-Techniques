'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.i0\ntorch.special.i0(input, *, out=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 10))
output = torch.special.i0(input_data)
print(output)