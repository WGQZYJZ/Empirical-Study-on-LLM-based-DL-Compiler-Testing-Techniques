'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sigmoid\ntorch.nn.Sigmoid()\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([1]), requires_grad=True)
y = torch.nn.Sigmoid()(x)
print(y)