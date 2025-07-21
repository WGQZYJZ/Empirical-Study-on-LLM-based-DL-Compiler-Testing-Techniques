'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(10, 10))
output = torch.frexp(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
input_data = np.random.randint(1, 10, (5, 5))
output = torch.from_numpy(input_data)
print(output)