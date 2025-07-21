'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
x = torch.randn(3, 5)
print(x)
softmax = torch.nn.Softmax(dim=1)
print(softmax(x))