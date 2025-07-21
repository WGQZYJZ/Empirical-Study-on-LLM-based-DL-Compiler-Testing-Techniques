'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
import torch
x = torch.rand(1, requires_grad=True)
torch.logit(x)
print(x)
print(torch.logit(x))
x.retain_grad()
print(x.grad)
x.retain_grad()
y = torch.logit(x)
y.backward()
print(x.grad)