'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
print(input)
output = torch.nn.functional.max_pool2d(input, 2)
print(output)
'\nTask 4: import PyTorch\nTask 5: Generate input data\nTask 6: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable