'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.zeros_\ntorch.nn.init.zeros_(tensor)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = torch.rand(5, 3)
print(x)
torch.nn.init.zeros_(x)
print(x)