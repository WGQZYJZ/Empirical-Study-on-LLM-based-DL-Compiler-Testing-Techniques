'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = (x * 2)
while (y.data.norm() < 1000):
    y = (y * 2)
print(y)
torch.set_printoptions(precision=10)
print(y)