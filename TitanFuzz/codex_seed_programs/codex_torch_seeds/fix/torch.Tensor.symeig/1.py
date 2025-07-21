'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.symeig\ntorch.Tensor.symeig(_input_tensor, eigenvectors=False, upper=True)\n'
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.randn(2, 2))
symeig_output = torch.Tensor.symeig(input_tensor, eigenvectors=True, upper=True)
print('input_tensor is: \n', input_tensor)
print('symeig_output is: \n', symeig_output)