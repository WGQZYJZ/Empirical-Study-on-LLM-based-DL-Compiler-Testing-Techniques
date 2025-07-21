'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 3), requires_grad=True)
print(x)
y = torch.nn.Threshold(0.5, 0)(x)
print(y)