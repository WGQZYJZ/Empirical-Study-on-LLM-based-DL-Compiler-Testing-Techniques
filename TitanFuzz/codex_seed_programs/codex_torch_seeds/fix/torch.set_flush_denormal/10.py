'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 5).cuda(), requires_grad=True)
y = Variable(torch.randn(5, 5).cuda(), requires_grad=True)
z = (x * y)
z = torch.sum(z)
z.backward()
print(x.grad.data)
torch.set_flush_denormal(True)
z = (x * y)
z = torch.sum(z)
z.backward()
print(x.grad.data)