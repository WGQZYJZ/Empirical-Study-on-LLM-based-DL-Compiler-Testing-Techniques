'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
output = torch.nn.functional.celu(input_data, alpha=1.0, inplace=False)
print(output)