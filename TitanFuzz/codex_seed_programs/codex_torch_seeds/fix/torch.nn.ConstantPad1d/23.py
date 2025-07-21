'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]))
print(input_data)
pad = torch.nn.ConstantPad1d(2, 0)
output = pad(input_data)
print(output)