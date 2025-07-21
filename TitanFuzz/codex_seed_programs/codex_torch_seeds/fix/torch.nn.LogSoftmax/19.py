'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
x = torch.randn(1, 3)
print(x)
print(torch.nn.LogSoftmax(dim=0)(x))
print(torch.nn.LogSoftmax(dim=1)(x))
print(torch.nn.LogSoftmax(dim=None)(x))
print(torch.nn.LogSoftmax(dim=(- 1))(x))
print(torch.nn.LogSoftmax(dim=(- 2))(x))