'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
x = torch.randn(3, requires_grad=True)
y = (x * 2)
with torch.no_grad():
    y = (x * 2)
    print(y)