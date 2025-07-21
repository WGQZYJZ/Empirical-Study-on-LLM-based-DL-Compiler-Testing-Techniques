'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sin_\ntorch.Tensor.sin_(_input_tensor)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.rand(3, 5))
torch.Tensor.sin_(input_tensor)
print('input_tensor: ', input_tensor)