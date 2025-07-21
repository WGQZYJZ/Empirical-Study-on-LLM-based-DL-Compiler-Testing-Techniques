"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.HuberLoss\ntorch.nn.HuberLoss(reduction='mean', delta=1.0)\n"
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([1]), requires_grad=True)
y = Variable(torch.Tensor([2]), requires_grad=True)
loss = torch.nn.HuberLoss(reduction='mean', delta=1.0)
output = loss(x, y)
print(output)
output.backward()
print(x.grad)
print(y.grad)