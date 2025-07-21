'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 32, 32))
print(x)
model = torch.nn.Sequential(torch.nn.Conv2d(1, 6, 5), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 2), torch.nn.Conv2d(6, 16, 5), torch.nn.ReLU(), torch.nn.MaxPool2d(2, 2), torch.nn.Flatten(), torch.nn.Linear(((16 * 5) * 5), 120), torch.nn.ReLU(), torch.nn.Linear(120, 84), torch.nn.ReLU(), torch.nn.Linear(84, 10))
print(model)