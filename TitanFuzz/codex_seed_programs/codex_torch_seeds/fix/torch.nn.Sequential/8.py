'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
model = torch.nn.Sequential(torch.nn.Linear(2, 2), torch.nn.ReLU(), torch.nn.Linear(2, 2))
y = model(x)
y.backward(torch.ones(2, 2))
print(x.grad)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Module\ntorch.nn.Module()\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable