'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = Variable(torch.Tensor(np.random.randn(5, 3)))
print(input_data)
selu = torch.nn.SELU(inplace=False)
output_data = selu(input_data)
print(output_data)