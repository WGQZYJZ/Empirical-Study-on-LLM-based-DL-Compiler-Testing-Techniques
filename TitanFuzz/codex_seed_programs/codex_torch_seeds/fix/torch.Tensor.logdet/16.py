'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_tensor = Variable(torch.randn(2, 3, 3))
print('Input tensor:')
print(input_tensor)
logdet_output = torch.Tensor.logdet(input_tensor)
print('Logdet output:')
print(logdet_output)