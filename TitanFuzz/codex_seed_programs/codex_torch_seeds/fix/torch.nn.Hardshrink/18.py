'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]))
print(input_data)
import torch
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]))
print(input_data)
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input_data)
print(output)