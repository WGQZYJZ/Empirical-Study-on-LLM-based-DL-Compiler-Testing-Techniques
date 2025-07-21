'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
import torch
input = torch.randn(2, 3)
print(input)
output = torch.nn.Softmax(dim=1)(input)
print(output)