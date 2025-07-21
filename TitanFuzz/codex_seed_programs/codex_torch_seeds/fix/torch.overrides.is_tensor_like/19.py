'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
from torch.autograd import Variable
from torch.autograd import Function
inp = torch.randn(3, 5)
torch.overrides.is_tensor_like(inp)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
from torch.autograd import Variable
from torch.autograd import Function
inp = Variable(torch.randn(3, 5))