'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.log_softmax\ntorch.special.log_softmax(input, dim, *, dtype=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.special.log_softmax(x, dim=0)
print('input data:', x)
print('output data:', y)