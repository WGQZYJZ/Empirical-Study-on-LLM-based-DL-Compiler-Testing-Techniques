'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_grad_enabled\ntorch.set_grad_enabled(mode)\n'
import torch
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0)
z = (x * y)
torch.set_grad_enabled(True)
z.backward()
print('x.grad: ', x.grad)
torch.set_grad_enabled(False)
print('x.grad: ', x.grad)