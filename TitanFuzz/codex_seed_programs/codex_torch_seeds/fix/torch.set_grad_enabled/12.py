'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_grad_enabled\ntorch.set_grad_enabled(mode)\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
torch.set_grad_enabled(True)
print(x.requires_grad)
torch.set_grad_enabled(False)
print(x.requires_grad)
y = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32, requires_grad=True)
print(y)
print(y.requires_grad)
with torch.no_grad():
    print((x ** 2).requires_grad)
x = torch.ones(2, 2, requires_grad=True)
print(x)
y = (x + 2)
print(y)
print(y.grad_fn)