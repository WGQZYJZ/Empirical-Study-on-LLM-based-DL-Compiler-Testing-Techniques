'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardshrink\ntorch.nn.functional.hardshrink(input, lambd=0.5)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
input_data = Variable(torch.randn(100, 100))
output_data = torch.nn.functional.hardshrink(input_data, lambd=0.5)
print(output_data)