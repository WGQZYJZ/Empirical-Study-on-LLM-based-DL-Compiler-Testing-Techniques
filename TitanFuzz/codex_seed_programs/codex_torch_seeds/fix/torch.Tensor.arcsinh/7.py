'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh\ntorch.Tensor.arcsinh(_input_tensor)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
output_data = torch.Tensor.arcsinh(input_data)
print(output_data)