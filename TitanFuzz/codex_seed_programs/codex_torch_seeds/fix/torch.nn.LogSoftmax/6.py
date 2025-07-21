'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSoftmax\ntorch.nn.LogSoftmax(dim=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
print(torch.nn.LogSoftmax(dim=1)(input))
print(torch.nn.LogSoftmax(dim=0)(input))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
input = torch.randn(2)
print(input)
print(torch.nn.Softplus()(input))
print(torch.nn.Softplus(beta=0.5, threshold=20)(input))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
input = torch.randn(2)
print(input)
print(torch.nn.Softshrink()(input))