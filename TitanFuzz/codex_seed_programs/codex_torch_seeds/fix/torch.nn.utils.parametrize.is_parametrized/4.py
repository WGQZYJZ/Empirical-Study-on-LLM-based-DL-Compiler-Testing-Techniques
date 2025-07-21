'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parametrize.is_parametrized\ntorch.nn.utils.parametrize.is_parametrized(module, tensor_name=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
torch.nn.utils.parametrize.is_parametrized(input_data)