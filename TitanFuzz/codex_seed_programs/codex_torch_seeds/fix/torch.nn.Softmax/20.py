'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
softmax = torch.nn.Softmax(dim=1)
output = softmax(input_data)
print('Output: ', output)
print('Sum of output: ', torch.sum(output, dim=1))