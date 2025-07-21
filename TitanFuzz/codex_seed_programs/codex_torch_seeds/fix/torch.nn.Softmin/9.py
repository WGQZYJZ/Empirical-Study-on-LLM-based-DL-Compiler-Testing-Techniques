'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
x = torch.randn(3, 5)
print('Input Data: ', x)
softmax = torch.nn.Softmin(dim=0)
output = softmax(x)
print('Softmax Output: ', output)
softmax = torch.nn.Softmin(dim=1)
output = softmax(x)
print('Softmax Output: ', output)