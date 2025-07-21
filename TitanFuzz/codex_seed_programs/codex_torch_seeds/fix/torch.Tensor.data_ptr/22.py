'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.data_ptr\ntorch.Tensor.data_ptr(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.rand(2, 3))
print(input_tensor)
print(input_tensor.data_ptr())
print(input_tensor.data_ptr())