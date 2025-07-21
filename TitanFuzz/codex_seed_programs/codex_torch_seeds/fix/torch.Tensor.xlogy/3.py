'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.xlogy\ntorch.Tensor.xlogy(_input_tensor, other)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_tensor = Variable(torch.rand(2, 3))
other_tensor = Variable(torch.rand(2, 3))
torch.Tensor.xlogy(input_tensor, other_tensor)
print(input_tensor)