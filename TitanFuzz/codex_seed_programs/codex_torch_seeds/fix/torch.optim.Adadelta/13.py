'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
import torch
x = torch.tensor(1.0, requires_grad=True)
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
optimizer = torch.optim.Adadelta([w, b], lr=0.1)
y = ((w * x) + b)
loss = (y - 4)
loss.backward()
optimizer.step()
print('w = ', w.item())
print('b = ', b.item())