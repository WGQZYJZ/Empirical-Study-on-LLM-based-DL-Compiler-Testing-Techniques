'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lgamma_\ntorch.Tensor.lgamma_(_input_tensor)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6]), requires_grad=True)
torch.Tensor.lgamma_(x)
print(x)