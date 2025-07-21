'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(1, 5))
torch.nn.functional.hardswish(input_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardtanh\ntorch.nn.functional.hardtanh(input, min_val=-1.0, max_val=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(1, 5))
torch.nn.functional.hardtanh(input_data)