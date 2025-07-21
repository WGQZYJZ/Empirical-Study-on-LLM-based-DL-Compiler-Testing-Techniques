'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 2))
torch.nn.functional.elu(x)
torch.nn.functional.elu(x, alpha=0.5)
torch.nn.functional.elu(x, alpha=0.5, inplace=True)
torch.nn.functional.elu(x, inplace=True)
torch.nn.functional.elu(x, alpha=0.5, inplace=False)
torch.nn.functional.elu(x, alpha=0.5)