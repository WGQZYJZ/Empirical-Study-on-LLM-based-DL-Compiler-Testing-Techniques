'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ParameterDict\ntorch.nn.ParameterDict(parameters=None)\n'
import torch
from torch.nn.parameter import Parameter
from torch.nn import ParameterDict
import torch
from torch.nn.parameter import Parameter
from torch.nn import ParameterDict
parameters = {'weight': Parameter(torch.randn(2, 2)), 'bias': Parameter(torch.randn(2))}
torch.nn.ParameterDict(parameters)