'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[2, 3, 4], [5, 6, 7]]))
print('Input data: ', input_data)
output = torch.nn.LogSoftmax(dim=1)(input_data)
print('Output: ', output)