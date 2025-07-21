'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
x = torch.Tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
print(x)
y = torch.nn.LogSoftmax(dim=1)(x)
print(y)