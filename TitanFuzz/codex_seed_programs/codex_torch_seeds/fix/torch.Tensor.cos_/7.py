'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos_\ntorch.Tensor.cos_(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(5, 3))
print(input_data)
print(torch.cos(input_data))
print(input_data.cos_())