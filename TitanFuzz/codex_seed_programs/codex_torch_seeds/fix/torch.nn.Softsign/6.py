'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(1, 5))
output = torch.nn.Softsign()(input)
print(output)