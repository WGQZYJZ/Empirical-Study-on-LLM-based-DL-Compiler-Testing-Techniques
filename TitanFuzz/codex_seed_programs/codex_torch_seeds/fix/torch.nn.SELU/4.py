'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
selu = torch.nn.SELU(inplace=False)
output = selu(input_data)
print(output)