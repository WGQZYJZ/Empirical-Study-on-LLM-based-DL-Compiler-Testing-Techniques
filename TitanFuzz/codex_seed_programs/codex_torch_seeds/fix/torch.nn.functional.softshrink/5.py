'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.randn(1, 10))
print(input_data)
softshrink_data = torch.nn.functional.softshrink(input_data, lambd=0.5)
print(softshrink_data)