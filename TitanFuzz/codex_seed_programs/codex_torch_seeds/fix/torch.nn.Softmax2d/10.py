'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
input = torch.randn(2, 3, 4, 4)
output = torch.nn.Softmax2d()(input)
print(output)