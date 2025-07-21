'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
import numpy as np
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.nn.Softmax(dim=0)(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
import numpy as np
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.nn.Softmax(dim=0)(x)
print(y)
y.backward(torch.tensor([1.0, 1.0, 1.0]))