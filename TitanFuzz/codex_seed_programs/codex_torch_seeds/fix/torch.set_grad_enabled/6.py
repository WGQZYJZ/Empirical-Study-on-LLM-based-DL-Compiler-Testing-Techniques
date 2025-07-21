'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_grad_enabled\ntorch.set_grad_enabled(mode)\n'
import torch
x = torch.tensor(1.0, requires_grad=True)
w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
y = ((w * x) + b)
y.backward()
print('dy/dx:', x.grad)
print('dy/dw:', w.grad)
print('dy/db:', b.grad)
with torch.no_grad():
    print('dy/dx:', x.grad)
    print('dy/dw:', w.grad)
    print('dy/db:', b.grad)
print('dy/dx:', x.grad)
print('dy/dw:', w.grad)