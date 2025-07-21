'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.parameters_to_vector\ntorch.nn.utils.parameters_to_vector(parameters)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(4, 4), requires_grad=True)
y = Variable(torch.randn(4, 4), requires_grad=True)
z = Variable(torch.randn(4, 4), requires_grad=True)
print(torch.nn.utils.parameters_to_vector([x, y, z]))