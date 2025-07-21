'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
input = torch.randn(1, 5, 3, 3)
print(input)
softmax2d = torch.nn.Softmax2d()
output = softmax2d(input)
print(output)