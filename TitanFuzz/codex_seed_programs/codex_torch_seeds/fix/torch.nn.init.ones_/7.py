'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
torch.nn.init.ones_(x)
print(x)