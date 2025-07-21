'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(4, 4))
index = Variable(torch.LongTensor([0, 2]))
value = Variable(torch.FloatTensor([0, 0]))
print(torch.Tensor.index_fill_(input_tensor, 0, index, value))